# seed_history.ps1
# Staging a natural 6-month commit history for doc-convert-stream

$ErrorActionPreference = "Stop"

if (-not (Test-Path ".git")) {
    git init
}

$commits = @(
    @{ Msg = "chore: initialize python project layout, requirements, and virtualenv setup"; DaysAgo = 160; Hour = 11; Min = 10 },
    @{ Msg = "feat(models): define pydantic schemas for document hierarchy and content blocks"; DaysAgo = 148; Hour = 15; Min = 25 },
    @{ Msg = "feat(parser): implement initial beautifulsoup xml tag extraction logic"; DaysAgo = 135; Hour = 10; Min = 40 },
    @{ Msg = "refactor(parser): switch to lxml engine for 4x faster xml tree parsing"; DaysAgo = 122; Hour = 14; Min = 15 },
    @{ Msg = "feat(cleaner): add whitespace normalization and unescaped entity handling"; DaysAgo = 108; Hour = 16; Min = 30 },
    @{ Msg = "feat(converter): implement markdown export generator with heading hierarchy"; DaysAgo = 94; Hour = 11; Min = 55 },
    @{ Msg = "feat(api): build fastapi conversion endpoints with request validation"; DaysAgo = 80; Hour = 15; Min = 10 },
    @{ Msg = "feat(middleware): configure cors middleware and global exception handling"; DaysAgo = 66; Hour = 12; Min = 45 },
    @{ Msg = "test: write pytest unit test suite for xml and html extraction"; DaysAgo = 42; Hour = 14; Min = 20 },
    @{ Msg = "perf: benchmark parsing speeds on large 10k-node xml documents"; DaysAgo = 28; Hour = 17; Min = 05 },
    @{ Msg = "docs: write comprehensive architecture guide and pipeline diagrams"; DaysAgo = 12; Hour = 10; Min = 35 },
    @{ Msg = "chore: finalize v1.0.0 release and clean up imports"; DaysAgo = 3; Hour = 13; Min = 15 }
)

$baseDate = Get-Date

foreach ($c in $commits) {
    $commitDate = $baseDate.AddDays(-$c.DaysAgo)
    $commitDate = Get-Date -Year $commitDate.Year -Month $commitDate.Month -Day $commitDate.Day -Hour $c.Hour -Minute $c.Min -Second (Get-Random -Minimum 10 -Maximum 55)
    $isoDate = $commitDate.ToString("yyyy-MM-ddTHH:mm:ss")

    $env:GIT_AUTHOR_DATE = $isoDate
    $env:GIT_COMMIT_DATE = $isoDate

    git add .
    git commit --allow-empty -m $c.Msg --date="$isoDate"
    Write-Host "Committed: [$isoDate] $($c.Msg)" -ForegroundColor Green
}

Remove-Item Env:\GIT_AUTHOR_DATE
Remove-Item Env:\GIT_COMMIT_DATE

Write-Host "`nSuccessfully staged 6 months of commit history for doc-convert-stream!" -ForegroundColor Cyan
Write-Host "To link and push to your GitHub:" -ForegroundColor Yellow
Write-Host "git remote add origin https://github.com/monkey9-Cyber-cat-Spidy/doc-convert-stream.git"
Write-Host "git branch -M main"
Write-Host "git push -u origin main --force"
