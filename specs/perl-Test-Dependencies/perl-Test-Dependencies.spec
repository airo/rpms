# $Id$
# Authority: dag
# Upstream: Zev Benjamin <zev@cpan.com>
# ExcludeDist: el4

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name Test-Dependencies

Summary: Ensure that your Makefile.PL specifies all module dependencies
Name: perl-Test-Dependencies
Version: 0.12
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/Test-Dependencies/

Source: http://www.cpan.org/modules/by-module/Test/Test-Dependencies-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl(B::PerlReq)
BuildRequires: perl(File::Find::Rule)
BuildRequires: perl(IPC::Cmd)
BuildRequires: perl(Module::CoreList)
BuildRequires: perl(PerlReq::Utils)
BuildRequires: perl(Pod::Strip)
BuildRequires: perl(Test::Builder::Module)
#BuildRequires: perl(Test::Builder::Tester) >= 0.64
BuildRequires: perl(Test::Builder::Tester)
BuildRequires: perl(YAML)
Requires: perl(B::PerlReq)
Requires: perl(File::Find::Rule)
Requires: perl(IPC::Cmd)
Requires: perl(Module::CoreList)
Requires: perl(PerlReq::Utils)
Requires: perl(Pod::Strip)
Requires: perl(Test::Builder::Module)
Requires: perl(YAML)

%filter_from_requires /^perl*/d
%filter_setup

%description
Ensure that your Makefile.PL specifies all module dependencies.

%prep
%setup -n %{real_name}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}" --skipdeps
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
%doc Changes MANIFEST META.yml README
%doc %{_mandir}/man3/Test::Dependencies.3pm*
%doc %{_mandir}/man3/Test::Dependencies::*.3pm*
%dir %{perl_vendorlib}/Test/
%{perl_vendorlib}/Test/Dependencies/
%{perl_vendorlib}/Test/Dependencies.pm

%changelog
* Wed Dec  9 2009 Christoph Maser <cmr@financial.com> - 0.12-1
- Updated to version 0.12.

* Fri Jan 04 2008 Dag Wieers <dag@wieers.com> - 0.11-1
- Updated to release 0.11.

* Sun Nov 18 2007 Dag Wieers <dag@wieers.com> - 0.08-1
- Initial package. (using DAR)
