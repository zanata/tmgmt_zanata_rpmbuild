%{?drupal7_find_provides_and_requires}

%global module tmgmt_zanata

Name:          drupal7-%{module}
Version:       1.10
Release:       1%{?dist}
Summary:       TMGMT Zanata is a plugin for Drupal's Translation Management Module TMGMT.

Group:         Applications/Publishing
License:       GPLv2+
URL:           http://drupal.org/project/%{module}
Source0:       http://ftp.drupal.org/files/projects/%{module}-7.x-%{version}.tar.gz
Source1:       %{name}-RPM-README.txt

BuildArch:     noarch
BuildRequires: drupal7-rpmbuild >= 7.23-3

# phpcompatinfo (computed from version 1.10)
#Requires:      php-

%description
TMGMT Zanata is a plugin for Drupal's Translation Management Module TMGMT. The
plugin allows TMGMT to send content to a configured Zanata project for
translation, and can download translations as they are ready.

Zanata is a web-based system for translators, content creators and developers
to manage localisation projects (see zanata.org).

This package provides the following Drupal module(s):
* %{module}


%prep
%setup -qn %{module}
cp -p %{SOURCE1} .


%build
# Empty build section, nothing to build


%install
mkdir -pm 0755 %{buildroot}%{drupal7_modules}/%{module}
cp -pr * %{buildroot}%{drupal7_modules}/%{module}/


%files
%doc *.txt
%{drupal7_modules}/%{module}
%exclude %{drupal7_modules}/%{module}/*.txt


%changelog
* Mon Jul 25 2016 David Mason <damason@redhat.com> 1.10-1
- Initial package

