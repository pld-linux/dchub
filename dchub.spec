Summary:	Direct Connect Hub
Summary(pl):	Serwer Direct Connect
Name:		dchub
Version:	0.4.5
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://ac2i.tzo.com/dctc/%{name}-%{version}.tar.gz
# Source0-md5:	ddad10cdebf1ac113e3343c1f83696a8
URL:		http://ac2i.tzo.com/dctc/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	python-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DCTC is a Direct Connect clone, a Windows client allowing users to
share their files and talk (like IRC but more software sharing
oriented) using a proprietary protocol.

%description -l pl
DCTC jest klonem Direct Connect, windowsowego klienta pozwalaj±cego
u¿ytkonikom dzieliæ pliki i rozmawiaæ (podobnie do IRC-a, ale w sposób
bardziej zorientowany na dzielenie oprogramowania) u¿ywaj±c w³asnego
protoko³u.

%prep
%setup -q

%build

%configure2_13

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO Documentation/*
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}/*
