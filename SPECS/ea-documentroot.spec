# This is the SPEC file that creates the RPM meta packages used
# by cPanel & WHM.  The RPMs should contain the configuration
# files, directory structures, and dependency tree needed to
# be compatible with cPanel & WHM devices.  You might consider
# this RPM package to be the "shim" that makes Apache and WHM
# work together.

%define webdocroot /var/www/html

%global ns_name  ea
%global pkg_name %{ns_name}-documentroot

# do not produce empty debuginfo package
%global debug_package %{nil}

Summary:       Package that installs error pages for Apache
Name:          %{pkg_name}
Version:       1.0
# Doing release_prefix this way for Release allows for OBS-proof versioning, See EA-4550 for more details
%define release_prefix 3
Release: %{release_prefix}%{?dist}.cpanel
Group:         System Environment/Daemons
License:       Apache License 2.0
Vendor:        cPanel, Inc.
BuildArch:     noarch

Source0:       400.shtml
Source1:       401.shtml
Source2:       403.shtml
Source3:       404.shtml
Source4:       413.shtml
Source5:       500.shtml
Source6:       cp_errordocument.shtml
Source7:       index.html

BuildRoot:     %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
#Requires:      ea-webserver

%description
This package contains error pages for Apache Web Server provided by cPanel

%install
rm -rf %{buildroot}

/bin/mkdir -p $RPM_BUILD_ROOT%{webdocroot}
install -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{webdocroot}/
install -m 644 %{SOURCE1} $RPM_BUILD_ROOT%{webdocroot}/
install -m 644 %{SOURCE2} $RPM_BUILD_ROOT%{webdocroot}/
install -m 644 %{SOURCE3} $RPM_BUILD_ROOT%{webdocroot}/
install -m 644 %{SOURCE4} $RPM_BUILD_ROOT%{webdocroot}/
install -m 644 %{SOURCE5} $RPM_BUILD_ROOT%{webdocroot}/
install -m 644 %{SOURCE6} $RPM_BUILD_ROOT%{webdocroot}/
install -m 644 %{SOURCE7} $RPM_BUILD_ROOT%{webdocroot}/

%clean
rm -rf %{buildroot}

%files
%defattr(0644, root, root)
%config(noreplace) %{webdocroot}/*

%changelog
* Mon Jun 20 2016 Dan Muey <dan@cpanel.net> - 1.0-3
- EA-4383: Update Release value to OBS-proof versioning

* Fri Aug 28 2015 S. Kurt Newman <kurt.newman@cpanel.net> 1.0-2
- Added missing index.html that displays cpanel default web page

* Mon May 18 2015 Joe Zhou <joe.zhou@cpanel.net> 1.0-1
- Set up the files
