Summary:	Direct Connect Hub
Summary(pl):	Serwer Direct Connect
Name:		dchub
Version:	0.5.2
Release:	1
License:	GPL
Group:		Applications/Communications
Source0:	http://ac2i.tzo.com/dctc/%{name}-%{version}.tar.gz
# Source0-md5:	673a43cde95bce2c2acba2cfab83d527
Patch0:		%{name}-configdir.patch
Patch1:		%{name}-init.patch
URL:		http://ac2i.tzo.com/dctc/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	glib2-devel
BuildRequires:	python-devel
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
dchub is a hub of direct connect file sharing network.

%description -l pl
dchub jest hubem sieci direct connect slu��cej do wymiany plik�w.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

%build
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d ${RPM_BUILD_ROOT}/%{_sysconfdir}/{%{name},rc.d/init.d}
install dchub.init $RPM_BUILD_ROOT/%{_sysconfdir}/rc.d/init.d/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install plugin/AUTOSTART $RPM_BUILD_ROOT/%{_libdir}/%{name}/plugins/AUTOSTART

mv $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/conf.xml.in \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/conf.xml
mv $RPM_BUILD_ROOT%{_sysconfdir}/%{name}/users.xml.in \
	$RPM_BUILD_ROOT%{_sysconfdir}/%{name}/users.xml

# delete unnecesary files
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/Makefile
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.c
rm -f $RPM_BUILD_ROOT%{_libdir}/%{name}/plugins/*.h
rm -rf $RPM_BUILD_ROOT%{_libdir}/%{name}/scripts/po

%post
if [ -f /var/lock/subsys/dchub ]; then
        /etc/rc.d/init.d/dchub restart >&2
fi

%preun                                                                          
if [ -f /var/lock/subsys/dchub ]; then
	/etc/rc.d/init.d/dchub stop >&2
fi

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%doc Documentation/{Global,commands,configuration_file,ext_prog,hub_cluster.postv0.4.0,plugin,protocol_extension,scripts,user_file}
%lang(de) %doc Documentation/*.de
%lang(fr) %doc Documentation/*.fr
%lang(nl) %doc Documentation/*.nl
%dir %{_sysconfdir}/%{name}
%config(noreplace) %verify(not md5 size mtime) %{_sysconfdir}/%{name}/*
%attr(755,root,root) %{_sysconfdir}/rc.d/init.d/%{name}
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/tools
%attr(755,root,root) %{_libdir}/%{name}/tools/*
%config(noreplace) %verify(not md5 size mtime) %{_libdir}/%{name}/extprog/AUTOSTART
%attr(755,root,root) %{_libdir}/%{name}/extprog/[CDPdm]*
%config(noreplace) %verify(not md5 size mtime) %{_libdir}/%{name}/plugins/AUTOSTART
%attr(755,root,root) %{_libdir}/%{name}/plugins/*.so
%dir %{_libdir}/%{name}/scripts
%attr(755,root,root) %{_libdir}/%{name}/scripts/*.pl
%config(noreplace) %verify(not md5 size mtime) %{_libdir}/%{name}/scripts/dchub_scripts.conf
%dir %{_libdir}/%{name}/scripts/i18n
%lang(de) %{_libdir}/%{name}/scripts/i18n/de
%lang(fr) %{_libdir}/%{name}/scripts/i18n/fr
%lang(hu) %{_libdir}/%{name}/scripts/i18n/hu
%lang(sv) %{_libdir}/%{name}/scripts/i18n/sv
