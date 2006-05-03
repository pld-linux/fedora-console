Summary:	Fedora DS Java Remote Management Console
Name:		fedora-console
Version:	1.0.2
Release:	0.1
License:	LGPL
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	cc2ccdf7a0f0a1ce78326251105a12f9
URL:		http://directory.fedora.redhat.com/wiki/Client_software
#BuildRequires:	jss >= 3.6
#BuildRequires:	ldapjdk >= 4.17
#Requires:	jss >= 3.6
#Requires:	ldapjdk >= 4.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Java based remote management console used for Managing Fedora
Administration Server and Fedora Directory Server.

%prep
%setup -q

%build
ant

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install built/release/jars/fedora-* $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}
install console/startconsole $RPM_BUILD_ROOT/%{_bindir}

cd $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s fedora-base-%{version}.jar fedora-base.jar
ln -s fedora-mcc-%{version}.jar fedora-mcc.jar
ln -s fedora-mcc-%{version}_en.jar fedora-mcc_en.jar
ln -s fedora-nmclf-%{version}.jar fedora-nmclf.jar
ln -s fedora-nmclf-%{version}_en.jar fedora-nmclf_en.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/%{name}/fedora-base-%{version}.jar
%{_datadir}/%{name}/fedora-mcc-%{version}.jar
%{_datadir}/%{name}/fedora-mcc-%{version}_en.jar
%{_datadir}/%{name}/fedora-nmclf-%{version}.jar
%{_datadir}/%{name}/fedora-nmclf-%{version}_en.jar
%{_datadir}/%{name}/fedora-base.jar
%{_datadir}/%{name}/fedora-mcc.jar
%{_datadir}/%{name}/fedora-mcc_en.jar
%{_datadir}/%{name}/fedora-nmclf.jar
%{_datadir}/%{name}/fedora-nmclf_en.jar
%attr(755,root,root) %{_bindir}/startconsole
