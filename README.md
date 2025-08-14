# Birthday Finder

A tiny, dependency-free web app. Enter your birth date and it shows:

- Day of the week you were born
- Days since your last birthday
- Days until your next birthday
- Age on your next birthday

Feb 29 birthdays are handled: in non-leap years, Feb 28 is used.

## Run

Just open `index.html` in your browser. No build needed.

On Windows, you can also start a lightweight local server (optional) for nicer file URLs:

```powershell
# from the project folder
powershell -NoProfile -Command "Add-Type -AssemblyName System.Net.HttpListener; $h=New-Object Net.HttpListener; $h.Prefixes.Add('http://localhost:8080/'); $h.Start(); Write-Host 'Serving on http://localhost:8080 (Ctrl+C to stop)'; while($h.IsListening){ $ctx=$h.GetContext(); $path=Join-Path (Get-Location) ($ctx.Request.Url.LocalPath.TrimStart('/')); if([string]::IsNullOrWhiteSpace($ctx.Request.Url.LocalPath) -or $ctx.Request.Url.LocalPath -eq '/'){$path='index.html'}; if(Test-Path $path){ $bytes=[System.IO.File]::ReadAllBytes($path); $ctx.Response.ContentType=([System.Web.MimeMapping]::GetMimeMapping($path)); $ctx.Response.OutputStream.Write($bytes,0,$bytes.Length)} else { $ctx.Response.StatusCode=404; $bytes=[Text.Encoding]::UTF8.GetBytes('Not Found'); $ctx.Response.OutputStream.Write($bytes,0,$bytes.Length)}; $ctx.Response.Close() }"
```

Or use any simple server you like.

## Notes

- Uses local time and local timezone.
- HTML date input relies on the browser; on older browsers you might see a plain text field.
