# $Id$
# Authority: dries
# Upstream: Austin Schutz <tex$habit,com>

%define perl_vendorlib %(eval "`perl -V:installvendorlib`"; echo $installvendorlib)
%define perl_vendorarch %(eval "`perl -V:installvendorarch`"; echo $installvendorarch)

%define real_name IO-Stty

Summary: Setting terminal parameters
Name: perl-IO-Stty
Version: .02
Release: 1
License: Artistic/GPL
Group: Applications/CPAN
URL: http://search.cpan.org/dist/IO-Stty/

Source: http://search.cpan.org/CPAN/authors/id/A/AU/AUSCHUTZ/IO-Stty-%{version}.tar.gz
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root

BuildArch: noarch
BuildRequires: perl

%description
The two perl items in this package are an stty shell script and a 
module for setting terminal parameters.

%prep
%setup -n %{real_name}-%{version}
%{__perl} -pi -e "s|/usr/local/perl/bin/perl|%{_bindir}/perl|g;" *.pl

%build
%{__perl} Makefile.PL INSTALLDIRS="vendor" PREFIX="%{buildroot}%{_prefix}"
%{__make} %{?_smp_mflags}

%install
%{__rm} -rf %{buildroot}
%makeinstall
%{__rm} -rf %{buildroot}%{perl_archlib} %{buildroot}%{perl_vendorarch}

%clean
%{__rm} -rf %{buildroot}

%files
%defattr(-, root, root, 0755)
%doc README
#%doc %{_mandir}/man3/*
%{perl_vendorlib}/IO/Stty.pm
%{perl_vendorlib}/IO/stty.pl

%changelog
* Sat Apr  9 2005 Dries Verachtert <dries@ulyssis.org> - .02-1
- Initial package.
