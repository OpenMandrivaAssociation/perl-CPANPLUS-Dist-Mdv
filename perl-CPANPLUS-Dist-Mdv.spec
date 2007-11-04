%define module  CPANPLUS-Dist-Mdv
%define name    perl-%{module}
%define version 0.1.3
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        A cpanplus backend to build mandriva rpms
License:        GPL or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/CPANPLUS/%{module}-%{version}.tar.gz
BuildRequires:  perl-version
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Readonly)
BuildRequires:  perl(CPANPLUS)
BuildRequires:  perl(YAML)
Buildarch:      noarch
BuildRoot:      %{_tmppath}/%{name}-%{version}

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
%setup -q -n %{module}-%{version}

%build
%{__perl} Build.PL installdirs=vendor
./Build

%install
rm -rf %{buildroot}
./Build install destdir=%{buildroot}

%check
./Build test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc Changes README
%{perl_vendorlib}/CPANPLUS
%{_mandir}/*/*

