Summary:	qoauth - Qt OAuth Support Library
Summary(pl.UTF-8):	qoauth - biblioteka Qt wsparcia dla OAuth
Name:		qoauth
Version:	1.0.1
Release:	1
License:	LGPL v2.1+
Group:		X11/Libraries
Source0:	http://files.ayoy.net/qoauth/release/current/src/%{name}-%{version}-src.tar.bz2
# Source0-md5:	bcb6d01e6c9a6fb22099c9e0f5889578
URL:		http://files.ayoy.net/qoauth/doc/
BuildRequires:	QtNetwork-devel
BuildRequires:	QtTest-devel
BuildRequires:	qca-devel >= 2.0.0
BuildRequires:	qt4-build >= 4.8.0
BuildRequires:	qt4-qmake >= 4.8.0
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
Requires:	qt4-qmake

%description devel
Header files for qoauth library.

%prep
%setup -q -n %{name}-%{version}-src

%build
qmake-qt4 qoauth.pro \
	QMAKE_CXX="%{__cxx}" \
	QMAKE_LINK="%{__cxx}" \
	QMAKE_CXXFLAGS_RELEASE="%{rpmcflags}" \
	QMAKE_LFLAGS_RPATH=

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc doc/examples README CHANGELOG
%attr(755,root,root) %{_libdir}/lib*.so.*

%files devel
%defattr(644,root,root,755)
%{_includedir}/QtOAuth
%{_datadir}/qt4/mkspecs/features/oauth.prf
%{_libdir}/lib*.so
%{_pkgconfigdir}/*.pc
