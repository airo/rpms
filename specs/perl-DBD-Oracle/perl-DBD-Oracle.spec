# $Id$
# Authority: dag
# Upstream: Pythian Remote DBA <pause$pythian,com>

%define perl_vendorlib %(eval "`%{__perl} -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`%{__perl} -V:installvendorarch`"; echo $installvendorarch)

%define real_name DBD-Oracle

Summary: Perl module named DBD-Oracle
Name: perl-DBD-Oracle
Version: 1.19
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/DBD-Oracle/

Source: http://www.cpan.org/modules/by-module/DBD/DBD-Oracle-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildRequires: perl

%description
perl-DBD-Oracle is a Perl module.

%prep
%setup -n %{real_name}-%{version}

%build
CFLAGS="%{optflags}" %{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags} OPTIMIZE="%{optflags}"

%install
%{__rm} -rf %{buildroot}
%{__make} pure_install

### Clean up buildroot
find %{buildroot} -name .packlist -exec %{__rm} {} \;

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc Changes MANIFEST MANIFEST.SKIP META.yml README README.aix.txt
%doc README.clients.txt README.explain.txt README.help.txt README.hpux.txt
%doc README.java.txt README.linux.txt README.login.txt README.longs.txt
%doc README.macosx.txt README.sec.txt README.vms.txt README.win32.txt
%doc README.wingcc.txt Todo
%doc %{_mandir}/man3/DBD::Oracle.3pm*
#%doc %{_mandir}/man3/*.3pm*
%dir %{perl_vendorarch}/DBD/
%{perl_vendorarch}/DBD/Oracle.pm
%dir %{perl_vendorarch}/auto/DBD/
%{perl_vendorarch}/auto/DBD/Oracle/

%changelog
* Sun Aug 05 2007 Dag Wieers <dag@wieers.com> - 1.19-1
- Initial package. (using DAR)