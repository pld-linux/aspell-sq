Summary:	Albanian dictionary for aspell
Summary(pl.UTF-8):	Słownik albański dla aspella
Name:		aspell-sq
Version:	0.1
Release:	2
License:	GPL v2
Group:		Applications/Text
Source0:	http://psychology.rutgers.edu/~zaimi/html/%{name}-%{version}.tgz
# Source0-md5:	40604173946cf75a2baa3f312ce724af
URL:		http://psychology.rutgers.edu/~zaimi/software.html
BuildRequires:	aspell >= 2:0.50
BuildRequires:	which
Requires:	aspell >= 2:0.50
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Albanian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik albański (lista słów) dla aspella.

%prep
%setup -q

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_prefix}/lib/aspell/sq.*
%{_datadir}/aspell/sq.dat
%{_datadir}/aspell/sq_phonet.dat
