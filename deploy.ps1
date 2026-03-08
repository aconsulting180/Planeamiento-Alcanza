# deploy.ps1 - Publica cambios en GitHub Pages con un solo comando
param(
    [string]$mensaje = "update: $(Get-Date -Format 'yyyy-MM-dd HH:mm')"
)

Write-Host "`n>> Preparando despliegue..." -ForegroundColor Cyan

# Verificar si hay cambios
$status = git status --porcelain
if (-not $status) {
    Write-Host "No hay cambios nuevos para publicar." -ForegroundColor Yellow
    exit 0
}

Write-Host "Archivos modificados:" -ForegroundColor Gray
git status --short

git add -A
git commit -m $mensaje
$result = git push 2>&1

if ($LASTEXITCODE -eq 0) {
    Write-Host "`n>> Publicado correctamente!" -ForegroundColor Green
    Write-Host ">> El sitio se actualizara en ~1-2 minutos en:" -ForegroundColor Green
    Write-Host "   https://aconsulting180.github.io/Planeamiento-Alcanza/" -ForegroundColor White
} else {
    Write-Host "`n>> Error al publicar:" -ForegroundColor Red
    Write-Host $result
}
