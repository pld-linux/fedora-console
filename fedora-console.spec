Summary:	Fedora DS Java Remote Management Console
Summary(pl):	Konsola w Javie do zdalnego zarz±dzania serwerem Fedora DS
Name:		fedora-console
Version:	1.0.3
Release:	0.1
License:	LGPL
Group:		Applications
Source0:	http://directory.fedora.redhat.com/sources/%{name}-%{version}.tar.gz
# Source0-md5:	3d3f05dc680dd09212aef7f0e271085e
URL:		http://directory.fedora.redhat.com/wiki/Client_software
BuildRequires:	ant >= 1.6
BuildRequires:	jdk
BuildRequires:	jpackage-utils
BuildRequires:	jss >= 3.3
BuildRequires:	ldapsdk >= 4.17
Requires:	jre
Requires:	jss >= 3.3
Requires:	ldapsdk >= 4.17
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A Java based remote management console used for Managing Fedora
Administration Server and Fedora Directory Server.

%description -l pl
Napisana w Javie konsola do zdalnego zarz±dzania serwerami Fedora
Administration Server i Fedora Directory Server.

%prep
%setup -q

%build
%ant \
	-Dbuilt.dir="`pwd`/built"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_datadir}/%{name}
install built/release/jars/fedora-* $RPM_BUILD_ROOT%{_datadir}/%{name}
install -d $RPM_BUILD_ROOT%{_bindir}
install startconsole $RPM_BUILD_ROOT%{_bindir}

cd $RPM_BUILD_ROOT%{_datadir}/%{name}
ln -s fedora-base-%{version}.jar fedora-base-1.0.jar
ln -s fedora-mcc-%{version}.jar fedora-mcc-1.0.jar
ln -s fedora-mcc-%{version}_en.jar fedora-mcc-1.0_en.jar
ln -s fedora-nmclf-%{version}.jar fedora-nmclf-1.0.jar
ln -s fedora-nmclf-%{version}_en.jar fedora-nmclf-1.0_en.jar

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/startconsole
%dir %{_datadir}/%{name}
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
