#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Math
%define	pnam	Pari
Summary:	Math::Pari - Perl interface to PARI.
Summary(pl.UTF-8):	Math:Pari - Perlowy interfejs do PARI.
Name:		perl-Math-Pari
Version:	2.010801
Release:	1
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Math/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	c0628a5ad79a53a22188aca476ea45ce
URL:		http://search.cpan.org/dist/Math-Pari/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package is a Perl interface to famous library PARI for
numerical/scientific/number-theoretic calculations.  It allows use of
most PARI functions as Perl functions, and (almost) seamless merging
of PARI and Perl data. In what follows we suppose prior knowledge of
what PARI is (see ftp://megrez.math.u-bordeaux.fr/pub/pari, or
Math::libPARI).

%description -l pl.UTF-8
Pakiet ten jest perlowym interfesjem do biblioteki PARI służącej do
obliczeń numerycznych/naukowych/liczbowo-teoretycznych.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make} \
	CC="%{__cc}" \
	OPTIMIZE="%{rpmcflags}"

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes INSTALL README TODO
%{perl_vendorarch}/Math/*.pm
%dir %{perl_vendorarch}/auto/Math/Pari
%{perl_vendorarch}/auto/Math/Pari/*.bs
%attr(755,root,root) %{perl_vendorarch}/auto/Math/Pari/*.so
%{_mandir}/man3/*
