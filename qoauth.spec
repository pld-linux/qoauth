
#%define snap rc2

Summary:	qoauth - Qt OAuth Support Library
Summary(pl.UTF-8):	qoauth - biblioteka Qt wsparcia dla OAuth
Name:		qoauth
Version:	0.1.0
Release:	0.1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://files.ayoy.net/qoauth/release/%{version}/src/%{name}-%{version}-src.tar.bz2
# Source0-md5:	0d0c8e6a1328d4c60984f4cb759a361a
URL:		http://files.ayoy.net/qoauth/doc/
BuildRequires:	QtNetwork-devel >= 4.3.0
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= 4.3.0
BuildRequires:	qt4-qmake >= 4.3.0
Requires:	qt4-plugin-qca-ossl >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Qt OAuth Support Library.

%description -l pl.UTF-8
Biblioteka Qt wsparcia dla OAuth.

%package devel
Summary:	Header files for qoauth library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for qoauth library.

%prep
%setup -q

%build
qmake-qt4 -unix -o Makefile %{name}.pro
%{__make} clean
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_libdir},%{_pkgconfigdir},%{_includedir}}

install lib/*.so* $RPM_BUILD_ROOT%{_libdir}
install include/* $RPM_BUILD_ROOT%{_includedir}
install *.pc $RPM_BUILD_ROOT%{_pkgconfigdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/examples doc/html README CHANGELOG
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/QtOAuth
%{_includedir}/%{name}*
%{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc
