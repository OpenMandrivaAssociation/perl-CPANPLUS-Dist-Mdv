%define upstream_name    CPANPLUS-Dist-Mdv
%define upstream_version 2.100400

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 2

Summary:    A cpanplus backend to build mandriva rpms
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:  perl(CPANPLUS)
BuildRequires:  perl(File::Find::Rule)
BuildRequires:  perl(File::HomeDir)
BuildRequires:  perl(File::ShareDir)
BuildRequires:  perl(File::Slurp)
BuildRequires:  perl(List::MoreUtils)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Pod::POM)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(Test::Script)
BuildRequires:  perl(YAML)
BuildRequires:  perl(version)

Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}

%description
CPANPLUS::Dist::Mdv is a distribution class to create mandriva packages from
CPAN modules, and all its dependencies. This allows you to have the most recent
copies of CPAN modules installed, using your package manager of choice, but
without having to wait for central repositories to be updated.

You can either install them using the API provided in this package, or manually
via rpm.

Some of the bleading edge CPAN modules have already been turned into mandriva
packages for you, and you can make use of them by adding the cooker
repositories (main & contrib).

Note that these packages are built automatically from CPAN and are assumed to
have the same license as perl and come without support. Please always refer to
the original CPAN package if you have questions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Build.PL installdirs=vendor
./Build

%check
./Build test

%install
%{__rm} -rf %{buildroot}
./Build install destdir=%{buildroot}

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README META.yml
%{perl_vendorlib}/CPANPLUS
%{perl_vendorlib}/auto
%{_mandir}/*/*


%changelog
* Sat May 28 2011 Funda Wang <fwang@mandriva.org> 2.100.400-2mdv2011.0
+ Revision: 680703
- mass rebuild

* Wed Feb 10 2010 Jérôme Quelin <jquelin@mandriva.org> 2.100.400-1mdv2011.0
+ Revision: 503766
- adding missing buildrequires:
- update to 2.100400

* Sun Nov 29 2009 Jérôme Quelin <jquelin@mandriva.org> 2.93.311-1mdv2010.1
+ Revision: 471047
- update to 2.093311

* Tue Jul 07 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.1-1mdv2010.0
+ Revision: 393195
- new version

* Mon Jul 06 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.2.0-1mdv2010.0
+ Revision: 392789
- new version

* Sun May 24 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.1.0-1mdv2010.0
+ Revision: 379210
- update to new version 1.1.0

* Mon Feb 02 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.0.0-1mdv2009.1
+ Revision: 336359
- update to new version 1.0.0

* Thu Nov 13 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.9-1mdv2009.1
+ Revision: 302820
- update to new version 0.3.9

* Mon Nov 10 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.8-1mdv2009.1
+ Revision: 301688
- new version

* Sun Nov 09 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.7-2mdv2009.1
+ Revision: 301465
- patch 0: force US format date in changelog
  patch 1: enforce mandriva summary format policy

* Sun Aug 10 2008 Jérôme Quelin <jquelin@mandriva.org> 0.3.7-1mdv2009.0
+ Revision: 270313
- update to new version 0.3.7

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.3.6-2mdv2009.0
+ Revision: 268377
- rebuild early 2009.0 package (before pixel changes)

* Wed Jun 11 2008 Jérôme Quelin <jquelin@mandriva.org> 0.3.6-1mdv2009.0
+ Revision: 218051
- update to new version 0.3.6

* Mon Feb 11 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.5-1mdv2008.1
+ Revision: 165058
- update to new version 0.3.5

* Wed Dec 26 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.4-1mdv2008.1
+ Revision: 138004
- update to new version 0.3.4

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Nov 27 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.3-1mdv2008.1
+ Revision: 113422
- update to new version 0.3.3
- update to new version 0.3.3

* Wed Nov 14 2007 Jérôme Quelin <jquelin@mandriva.org> 0.3.2-1mdv2008.1
+ Revision: 108635
- added new prereq
- update to new version 0.3.2

* Sun Nov 11 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.3.0-1mdv2008.1
+ Revision: 108015
- update to new version 0.3.0
- update to new version 0.3.0

* Thu Nov 08 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.2-1mdv2008.1
+ Revision: 106875
- update to new version 0.2.2

* Tue Nov 06 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.2.1-1mdv2008.1
+ Revision: 106549
- new version

* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.3-1mdv2008.1
+ Revision: 105821
- import perl-CPANPLUS-Dist-Mdv


* Sun Nov 04 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.1.3-1mdv2008.1
- first mdv release 
