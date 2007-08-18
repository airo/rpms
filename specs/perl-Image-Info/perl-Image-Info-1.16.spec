# $Id$
# Authority: dries
# Upstream: Gisle Aas <gisle$activestate,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name Image-Info

Summary: Extract meta information from image files
Name: perl-Image-Info
Version: 1.16
Release: 2
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Image-Info/

Source: http://www.cpan.org/modules/by-module/Image/Image-Info-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
This Perl extention allows you to extract meta information from
various types of image files.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall

### Clean up buildroot
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/Image/
%{perl_vendorlib}/Image/Info.pm
%{perl_vendorlib}/Image/Info/
%{perl_vendorlib}/Image/TIFF.pm

%changelog
* Sat Jan 01 2005 Dries Verachtert <dries@ulyssis.org> - 1.16-2
- Fixed the license tag (Thanks to David Necas !)

* Fri Dec 10 2004 Dries Verachtert <dries@ulyssis.org> - 1.16-1
- Initial package.