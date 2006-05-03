Summary:	Fedora DS Java Remote Management Console
Name:		fedora-console
Version:	1.0.2
Release:	0.1
License:	LGPL
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	cc2ccdf7a0f0a1ce78326251105a12f9
Source1:	ftp://ftp.mozilla.org/pub/mozilla.org/security/jss/releases/JSS_3_3_RTM/jss33.jar
# Source1-md5:	efcae3a220aba17bf98cdcb6c36fc55e
URL:		http://directory.fedora.redhat.com/wiki/Client_software
BuildRequires:	jakarta-ant >= 1.6
#BuildRequires:	jss >= 3.6
BuildRequires:	ldapsdk >= 4.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Java based remote management console used for Managing Fedora
Administration Server and Fedora Directory Server.

%prep
%setup -q
install %{SOURCE1} ./jss3.jar

%build
ant -Djss.local.location=.

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install ../built/release/jars/fedora-* $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}
install startconsole $RPM_BUILD_ROOT/%{_bindir}

cd $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s fedora-base-1.0.jar fedora-base-%{version}.jar
ln -s fedora-mcc-1.0.jar fedora-mcc-%{version}.jar
ln -s fedora-mcc-1.0_en.jar fedora-mcc-%{version}_en.jar
ln -s fedora-nmclf-1.0.jar fedora-nmclf-%{version}.jar
ln -s fedora-nmclf-1.0_en.jar fedora-nmclf-%{version}_en.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_datadir}/%{name}/fedora-base-%{version}.jar
%{_datadir}/%{name}/fedora-mcc-%{version}.jar
%{_datadir}/%{name}/fedora-mcc-%{version}_en.jar
%{_datadir}/%{name}/fedora-nmclf-%{version}.jar
%{_datadir}/%{name}/fedora-nmclf-%{version}_en.jar
%{_datadir}/%{name}/fedora-base-1.0.jar
%{_datadir}/%{name}/fedora-mcc-1.0.jar
%{_datadir}/%{name}/fedora-mcc-1.0_en.jar
%{_datadir}/%{name}/fedora-nmclf-1.0.jar
%{_datadir}/%{name}/fedora-nmclf-1.0_en.jar
%attr(755,root,root) %{_bindir}/startconsole
