Summary:	Direct Connect Hub
Summary(pl):	Serwer Direct Connect
Name:		dchub
Version:	0.2.0
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://ac2i.tzo.com/dctc/%{name}-%{version}.tar.gz
# Source0-md5:	2c977e0fe0ed429af4a05c5920c1e855
#Patch0:		%{name}-home_etc.patch
URL:		http://ac2i.tzo.com/dctc/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	glib-devel
BuildRequires:	python-devel
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
#%patch0 -p1

%build
./configure --prefix=/usr
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
#%doc KNOWN_BUGS TODO README ChangeLog Documentation/* Documentation/*/*
%attr(755,root,root) %{_bindir}/*
