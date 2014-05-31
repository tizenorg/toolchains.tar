#
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.22
#

Name:       tar
Summary:    A GNU file archiving program
Version:    1.17
Release:    4
Epoch:      1
Group:      Applications/Archiving
License:    GPLv2+
URL:        http://www.gnu.org/software/tar/
Source0:    ftp://ftp.gnu.org/pub/gnu/tar/tar-%{version}.tar.gz
Source1:    tar.1
Source1001:     %{name}.manifest
Patch0:     tar-1.14-loneZeroWarning.patch
Patch1:     tar-1.15.1-vfatTruncate.patch
Patch2:     tar-1.17-testsuite.patch
Patch3:     tar-1.17-xattrs.patch
Patch4:     tar-1.17-wildcards.patch
Patch5:     tar-1.17-dot_dot_vuln.patch
Patch6:     gcc43.patch
Patch7:     tar-1.17-gcc4.patch
Patch8:     BMC6647-CVE-2010-0624.patch
Patch9:     BMC6661-CVE-2007-4476.patch
BuildRequires:  libacl-devel

%description
The GNU tar program saves many files together in one archive and can
restore individual files (or all of the files) from that archive. Tar
can also be used to add supplemental files to an archive and to update
or list files in the archive. Tar includes multivolume support,
automatic archive compression/decompression, the ability to perform
remote archives, and the ability to perform incremental and full
backups.

If you want to use tar for remote backups, you also need to install
the rmt package.


%prep
%setup -q -n %{name}-%{version}

# tar-1.14-loneZeroWarning.patch
%patch0 -p1
# tar-1.15.1-vfatTruncate.patch
%patch1 -p1
# tar-1.17-testsuite.patch
%patch2 -p1
# tar-1.17-xattrs.patch
%patch3 -p1
# tar-1.17-wildcards.patch
%patch4 -p1
# tar-1.17-dot_dot_vuln.patch
%patch5 -p1
# gcc43.patch
%patch6 -p1
# tar-1.17-gcc4.patch
%patch7 -p1
# BMC6647-CVE-2010-0624.patch
%patch8 -p1
# BMC6661-CVE-2007-4476.patch
%patch9 -p1

%build
cp %{SOURCE1001} .
%configure --disable-static \
    --bindir=/bin \
    --disable-nls

make %{?jobs:-j%jobs}

%install
rm -rf %{buildroot}
%make_install
mkdir -p %{buildroot}%{_mandir}/man1
cp -a %{SOURCE1} %{buildroot}%{_mandir}/man1

rm -rf %{buildroot}%{_prefix}/libexec/rmt

mkdir -p $RPM_BUILD_ROOT%{_datadir}/license
for keyword in LICENSE COPYING COPYRIGHT;
do
	for file in `find %{_builddir} -name $keyword`;
	do
		cat $file >> $RPM_BUILD_ROOT%{_datadir}/license/%{name};
		echo "";
	done;
done

%docs_package

%files
%manifest %{name}.manifest
%defattr(-,root,root,-)
%{_datadir}/license/%{name}
/bin/tar


