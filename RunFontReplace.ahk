^y::
loop, 22
{
    Send, ^+I
    Sleep, 100
    Send, %A_index%
    SendRaw, .svg
    Send, {Enter}
    Sleep, 100
    Send, {Right}
}
