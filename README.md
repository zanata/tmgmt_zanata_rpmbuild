# tmgmt_zanata_rpmbuild

RPM building artefacts for tmgmt_zanata, such as spec files and the readme.


## Prerequisites

This assumes you are running on Red Hat Enterprise Linux 6.
Other platforms may work but are not tested or supported for this module.

EPEL repository must be enabled.
[EPEL setup instructions here](http://fedoraproject.org/wiki/EPEL#How_can_I_use_these_extra_packages.3F)


## Setup

Install RPM building tools for Drupal 7, and create the required directories:

```
sudo yum install rpm-build rpmdevtools drupal7-rpmbuild
rpmdev-setuptree
```

## Building an RPM

1. Copy the spec file from this repository to `~/rpmbuild/SPECS`.
2. Copy the readme file from this repository to `~/rpmbuild/SOURCES`.
3. Download the release archive to `~/rpmbuild/SOURCES`. Find the
   archive on the [tmgmt_zanata homepage](https://www.drupal.org/project/tmgmt_zanata).
4. In `~/rpmbuild/SPECS`, run `rpmbuild -ba drupal7-tmgmt_zanata.spec`
5. The built rpm and source rpm should now be in `~/rpmbuild/RPMS` and `~/rpmbuild/SRPMS`.
