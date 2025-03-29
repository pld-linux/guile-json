Summary:	Guile JSON implementation
Summary(pl.UTF-8):	Implementacja JSON dla języka Guile
Name:		guile-json
Version:	4.7.3
Release:	1
License:	GPL v3+
Group:		Libraries
#Source0Download: https://github.com/aconchillo/guile-json/tags
Source0:	https://github.com/aconchillo/guile-json/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	69093e6eb134a37224d73fe393fb39db
Patch0:		%{name}-am.patch
URL:		https://github.com/aconchillo/guile-json
BuildRequires:	autoconf >= 2.50
BuildRequires:	automake >= 1:1.11
BuildRequires:	guile-devel >= 5:2.0
BuildRequires:	guile-devel < 5:3.2
BuildRequires:	pkgconfig
Requires:	guile-libs >= 5:2.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
guile-json is a JSON module for Guile. It supports parsing and
building JSON documents according to the <http://json.org/>
specification.

%description -l pl.UTF-8
guile-json to moduł JSON dla języka Guile. Obsługuje analizę i
tworzenie dokumentów JSON zgodnie ze specyfikacją <http://json.org/>.

%prep
%setup -q
%patch -P0 -p1

install -d build-aux

%build
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README.md
%{_libdir}/guile/*.*/site-ccache/json.go
%{_libdir}/guile/*.*/site-ccache/json
%{_datadir}/guile/site/*.*/json.scm
%{_datadir}/guile/site/*.*/json
