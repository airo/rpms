# $Id$
# Authority: dag
# Upstream: Stevan Little E<lt>stevan$iinteractive,comE<gt>
# Upstream: Brandon L, Black, E<lt>blblack$gmail,comE<gt>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name MooseX-Getopt

Summary: A Moose role for processing command line options
Name: perl-MooseX-Getopt
Version: 0.05
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/MooseX-Getopt/

Source: http://www.cpan.org/modules/by-module/MooseX/MooseX-Getopt-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl
BuildRequires: perl(Test::More) >= 0.62
BuildRequires: perl(Test::Exception) >= 0.21

%description
A Moose role for processing command line options.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc ChangeLog MANIFEST MANIFEST.SKIP META.yml README
%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorlib}/MooseX/
%{perl_vendorlib}/MooseX/Getopt/
%{perl_vendorlib}/MooseX/Getopt.pm

%changelog
* Sat Aug 04 2007 Dag Wieers <dag@wieers.com> - 0.05-1
- Initial package. (using DAR)