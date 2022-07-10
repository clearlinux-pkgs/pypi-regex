#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pypi-regex
Version  : 2022.7.9
Release  : 44
URL      : https://files.pythonhosted.org/packages/52/b1/48941b5df2d73a14e067e68d9055544effc515c8242741fd7c1dd2d72101/regex-2022.7.9.tar.gz
Source0  : https://files.pythonhosted.org/packages/52/b1/48941b5df2d73a14e067e68d9055544effc515c8242741fd7c1dd2d72101/regex-2022.7.9.tar.gz
Summary  : Alternative regular expression module, to replace re.
Group    : Development/Tools
License  : Apache-2.0
Requires: pypi-regex-filemap = %{version}-%{release}
Requires: pypi-regex-lib = %{version}-%{release}
Requires: pypi-regex-license = %{version}-%{release}
Requires: pypi-regex-python = %{version}-%{release}
Requires: pypi-regex-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : python3-dev

%description
Introduction
------------
This regex implementation is backwards-compatible with the standard 're' module, but offers additional functionality.

%package filemap
Summary: filemap components for the pypi-regex package.
Group: Default

%description filemap
filemap components for the pypi-regex package.


%package lib
Summary: lib components for the pypi-regex package.
Group: Libraries
Requires: pypi-regex-license = %{version}-%{release}
Requires: pypi-regex-filemap = %{version}-%{release}

%description lib
lib components for the pypi-regex package.


%package license
Summary: license components for the pypi-regex package.
Group: Default

%description license
license components for the pypi-regex package.


%package python
Summary: python components for the pypi-regex package.
Group: Default
Requires: pypi-regex-python3 = %{version}-%{release}

%description python
python components for the pypi-regex package.


%package python3
Summary: python3 components for the pypi-regex package.
Group: Default
Requires: pypi-regex-filemap = %{version}-%{release}
Requires: python3-core
Provides: pypi(regex)

%description python3
python3 components for the pypi-regex package.


%prep
%setup -q -n regex-2022.7.9
cd %{_builddir}/regex-2022.7.9
pushd ..
cp -a regex-2022.7.9 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1657480316
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=auto "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=auto "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=auto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 setup.py build

popd
%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pypi-regex
cp %{_builddir}/regex-2022.7.9/LICENSE.txt %{buildroot}/usr/share/package-licenses/pypi-regex/692d7ee2ea91449bb8354092cedb2fd1f5a7a2e0
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
pushd ../buildavx2/
export CFLAGS="$CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export CXXFLAGS="$CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FFLAGS="$FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
export FCFLAGS="$FCFLAGS -m64 -march=x86-64-v3 "
export LDFLAGS="$LDFLAGS -m64 -march=x86-64-v3 "
python3 -tt setup.py build install --root=%{buildroot}-v3
popd
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files filemap
%defattr(-,root,root,-)
/usr/share/clear/filemap/filemap-pypi-regex

%files lib
%defattr(-,root,root,-)
/usr/share/clear/optimized-elf/other*

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pypi-regex/692d7ee2ea91449bb8354092cedb2fd1f5a7a2e0

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
