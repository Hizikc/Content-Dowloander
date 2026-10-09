[Setup]
AppName=Content Downloader
AppVersion=1.0.0
AppPublisher=hizikc
DefaultDirName={autopf}\Content Downloader
DefaultGroupName=Content Downloader
AllowNoIcons=yes
OutputDir=.
OutputBaseFilename=Content_Downloader_Setup
Compression=lzma
SolidCompression=yes
WizardStyle=modern
SetupIconFile=assets\logo.ico

[Files]
Source: "docs\Content-Downloader.exe"; DestDir: "{app}"; Flags: ignoreversion
Source: "assets\logo.ico"; DestDir: "{app}"; Flags: ignoreversion

[Icons]
Name: "{group}\Content Downloader"; Filename: "{app}\Content-Downloader.exe"; IconFilename: "{app}\logo.ico"
Name: "{autodesktop}\Content Downloader"; Filename: "{app}\Content-Downloader.exe"; Tasks: desktopicon; IconFilename: "{app}\logo.ico"

[Tasks]
Name: "desktopicon"; Description: "Создать ярлык на рабочем столе"; Flags: unchecked

[Run]
Filename: "{app}\Content-Downloader.exe"; Description: "Запустить программу"; Flags: nowait postinstall skipifsilent
