Summary:	Direct Connect Hub
Summary(pl):	Serwer Direct Connect
Name:		dchub
Version:	0.5.0
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://ac2i.tzo.com/dctc/%{name}-%{version}.tar.gz
# Source0-md5:	bc03737a91e39b7f9d2c0a8abbbac101
URL:		http://ac2i.tzo.com/dctc/
#BuildRequires:	autoconf
#BuildRequires:	automake
BuildRequires:	glib2-devel
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
%doc AUTHORS ChangeLog NEWS README TODO
%doc Documentation/{Global,commands,configuration_file,ext_prog,hub_cluster.postv0.4.0,plugin,protocol_extension,scripts,user_file}
%lang(de) %doc Documentation/*.de
%lang(fr) %doc Documentation/*.fr
%lang(nl) %doc Documentation/*.nl
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%{_libdir}/%{name}/extprog
%{_libdir}/%{name}/plugins
%dir %{_libdir}/%{name}/scripts
%{_libdir}/%{name}/scripts/*.pl
%{_libdir}/%{name}/scripts/*.py
%{_libdir}/%{name}/scripts/*.conf
%dir %{_libdir}/%{name}/scripts/i18n
%lang(de) %{_libdir}/%{name}/scripts/i18n/de
%lang(fr) %{_libdir}/%{name}/scripts/i18n/fr
%lang(hu) %{_libdir}/%{name}/scripts/i18n/hu
%lang(sv) %{_libdir}/%{name}/scripts/i18n/sv
# these are installed, are really needed???
%dir %{_libdir}/%{name}/scripts/po
%{_libdir}/%{name}/scripts/po/*.pl
%{_libdir}/%{name}/scripts/po/*.sh
%{_libdir}/%{name}/scripts/po/*.pot
%lang(de) %{_libdir}/%{name}/scripts/po/de.po
%lang(fr) %{_libdir}/%{name}/scripts/po/fr.po
%lang(hu) %{_libdir}/%{name}/scripts/po/hu.po
%lang(sv) %{_libdir}/%{name}/scripts/po/sv.po
