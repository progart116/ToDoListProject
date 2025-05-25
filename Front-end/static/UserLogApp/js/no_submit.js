function NoSubmit(event)
{
    if (event.keyCode == 13)
    {
        event.preventDefault();
        return false;
    }
}