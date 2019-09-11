const HKEY_LOCAL_MACHINE = &H80000002
Dim strComputer, strKeyPath
Dim objReg, strSubkey, arrSubkeys 
Dim Name, Version, vm, ipval, chrome, ie, browser 

vm = 0
chrome = -1
ie = 0
ipval = 0
browser = 0
strComputer = "."
 
' Registry key path of Control panel items for installed programs
strKeyPath = "Software\Wow6432Node\Microsoft\Windows\CurrentVersion\Uninstall\" 
 
Set objReg=GetObject( _ 
    "winmgmts:{impersonationLevel=impersonate}!\\" & _
   strComputer & "\root\default:StdRegProv")
 
objReg.EnumKey HKEY_LOCAL_MACHINE, strKeyPath, arrSubkeys 

If isArray(arrSubkeys) Then
	if UBound(arrSubkeys) < 0 Then
 		strKeyPath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\"
		objReg.EnumKey HKEY_LOCAL_MACHINE, strKeyPath, arrSubkeys 
	End If
Else
           strKeyPath = "SOFTWARE\Microsoft\Windows\CurrentVersion\Uninstall\"
		objReg.EnumKey HKEY_LOCAL_MACHINE, strKeyPath, arrSubkeys 
End If

'Enumerate registry keys.
For Each strSubkey In arrSubkeys 
 objReg.GetStringValue HKEY_LOCAL_MACHINE, strKeyPath & strSubkey, "DisplayName" , Name
 If InStr(Name,"VMware Horizon Client") Then
 
 objReg.GetStringValue HKEY_LOCAL_MACHINE, strKeyPath & strSubkey,"DisplayVersion",Version

 If Split(Version,".")(0) >= 4 Then
	vm = 1	
	
		 result = MsgBox ("VMWare Horizon Tool is available in you machine. Do you want to open it?", vbYesNo + vbQuestion, "Learning Lab")

Select Case result

Case vbYes
	
    Set WshShell = WScript.CreateObject("WScript.Shell")
	Dim exeName 
	Dim statusCode
	exeName = """C:\Program Files\VMware\VMware Horizon View Client\vmware-view.exe"""
	
	On Error Resume Next
	statusCode = WshShell.Run (exeName, 1, true)
	
	If Err.Number <> 0 Then
  		exeName = """C:\Program Files (x86)\VMware\VMware Horizon View Client\vmware-view.exe"""
  		statusCode = WshShell.Run (exeName, 1, true)
	End If
	
	On Error Goto 0

	WScript.Quit 1
Case vbNo
    
End Select
		
 End If 
End If

 If InStr(Name,"Chrome") Then
 chrome = 0
 objReg.GetStringValue HKEY_LOCAL_MACHINE, strKeyPath & strSubkey,"DisplayVersion",Version
 If Split(Version,".")(0) >= 58 Then
 chrome = 1
 End If
End If

Next 

Set oReg=GetObject("winmgmts:{impersonationLevel=impersonate}!\\"&strComputer & "\root\default:StdRegProv")
strKeyPath = "SOFTWARE\Microsoft\Internet Explorer"
strValueName = "Version"
oReg.GetStringValue HKEY_LOCAL_MACHINE,strKeyPath,strValueName,strValue
If Left(strValue,1) >= 9 Then
 ie = 1
End If

dim NIC1, Nic, StrIP, CompName, port
Set NIC1 =     GetObject("winmgmts:").InstancesOf("Win32_NetworkAdapterConfiguration")
For Each Nic in NIC1

    if Nic.IPEnabled then
        StrIP = Nic.IPAddress(i)
	IP = Split(StrIP,".")(0)
	If IP = 10 Then
	ipval = 1
	End If
    End if
Next  


if ie = 1 OR chrome = 1 Then
browser = 1
End if

Set browobj = CreateObject("Wscript.Shell")
'browobj.Run "https://assessmentuat.cognizant.com/mylab/WebContent/Index1.html?vm="&vm&"&browser="&browser&"&ipval="&ipval
browobj.Run "chrome -url https://learninglabs.cognizant.com/learninglab/Result.html?vm="&vm&"&browser="&browser&"&ipval="&ipval
