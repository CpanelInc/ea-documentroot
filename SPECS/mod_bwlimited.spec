%global ns_name ea

Summary: Provides cPanel's default document roots
Name: ea-mod_documentroot
Version: 1.0
Release: 1%{?dist}
License: Unknown
Group: System Environment/Daemons
URL: http://cpanel.net/
#Source0: 
Requires: ea-apache2

%description
This RPM provides cPanel's default error pages

%prep
%setup -q -n

%build

%install

%files

%changelog
* Wed Nov 26 2014 Matt Dees <matt@cpanel.net> - 1.0-1
* Implement skeleton spec
