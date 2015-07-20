ServerAccess

Typcical usage:

    server_access = ServerAccess('host', 'username', 'pw')

    # Install git
    if not server.is_git_installed():
        server.install_git()

    # Remove git
    if server.is_git_installed()
        server.remove_git()

    # Run Terminal commands directly
    server_access = ServerAccess('host', 'username', 'pw')
    response, error = server_access.run("uname -s")
    response, error = server_access.run("uptime")
    response, error = server_access.run("ls")
    response, error = server_access.run("git --version")

    # Run terminal command as sudo (don't include sudo in string)
    print server_access.run_sudo("dmesg")