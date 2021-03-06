# $Id: gnome-commander.spec 7439 2009-07-14 11:35:07Z dag $
# Authority: dag

Summary: File manager for the GNOME desktop
Name: gnome-commander
Version: 1.2.8.12
Release: 1%{?dist}
License: GPL
Group: Applications/File
URL: http://www.nongnu.org/gcmd/

Source: http://ftp.gnome.org/pub/GNOME/sources/gnome-commander/1.2/gnome-commander-%{version}.tar.bz2
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: gcc-c++
BuildRequires: gettext >= 0.10.36
BuildRequires: glib2-devel >= 2.6
BuildRequires: gnome-doc-utils >= 0.3.2
BuildRequires: gnome-vfs2-devel >= 2.0
BuildRequires: intltool
BuildRequires: libgnomeui-devel >= 2.0
BuildRequires: scrollkeeper

Requires: desktop-file-utils
Requires: scrollkeeper

%description
GNOME Commander is a nice and fast file manager for the GNOME desktop.
In addition to performing the basic filemanager functions the program
is also an FTP-client and it can browse SMB-networks.

%prep
%setup

%build
%configure \
    --disable-scrollkeeper
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} install DESTDIR="%{buildroot}"
%find_lang %{name}

%post
scrollkeeper-update -q -o %{_datadir}/omf/gnome-commander/ || :
/usr/bin/update-desktop-database -q || :

%postun
scrollkeeper-update -q || :
/usr/bin/update-desktop-database -q || :

%clean
%{__rm} -rf %{buildroot}

%files -f %{name}.lang
%defattr(-, root, root, 0755)
%doc AUTHORS BUGS ChangeLog COPYING INSTALL NEWS README TODO doc/*.txt
%doc %{_mandir}/man1/gnome-commander.1*
%doc %{_datadir}/gnome/help/gnome-commander/
%{_bindir}/gcmd-block
%{_bindir}/gnome-commander
%{_libdir}/gnome-commander/
%{_datadir}/applications/gnome-commander.desktop
%{_datadir}/omf/gnome-commander/
%{_datadir}/pixmaps/gnome-commander/
%{_datadir}/pixmaps/gnome-commander.png

%changelog
* Sun Jun 19 2011 Dag Wieers <dag@wieers.com> - 1.2.8.12-1
- Updated to release 1.2.8.12.

* Mon May 02 2011 Dag Wieers <dag@wieers.com> - 1.2.8.11-1
- Updated to release 1.2.8.11.

* Wed Jan 26 2011 Dag Wieers <dag@wieers.com> - 1.2.8.10-1
- Updated to release 1.2.8.10.

* Sat Dec 04 2010 Dag Wieers <dag@wieers.com> - 1.2.8.9-1
- Updated to release 1.2.8.9.

* Thu Jun 03 2010 Dag Wieers <dag@wieers.com> - 1.2.8.3-2
- Rebuild against exiv2-0.20.

* Thu Oct 29 2009 Dag Wieers <dag@wieers.com> - 1.2.8.3-1
- Updated to release 1.2.8.3.

* Fri Jul 10 2009 Dag Wieers <dag@wieers.com> - 1.2.7-2
- Rebuild against exiv2-0.18.2.

* Wed Jul 30 2008 Heiko Adams <info-2K8@ha-software.de> 1.2.7-1
- Updated to release 1.2.7.

* Sun Jun 01 2008 Heiko Adams <info-2K8@ha-software.de> 1.2.6-1
- Updated to release 1.2.6.

* Fri Feb 29 2008 Heiko Adams <info-2007@ha-software.de> 1.2.5-1
- Updated to release 1.2.5.

* Sun Jun 10 2007 Dag Wieers <dag@wieers.com> 1.2.4-1
- Updated to release 1.2.4.

* Mon Dec 11 2006 Dag Wieers <dag@wieers.com> 1.2.2-1
- Initial package. (using DAR)
