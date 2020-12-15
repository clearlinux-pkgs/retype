#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : retype
Version  : 20.10.0
Release  : 29
URL      : https://files.pythonhosted.org/packages/c0/0f/9c896ff833df93389aec01768d40a39567f9abcce8f4318e8139e50e8726/retype-20.10.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/c0/0f/9c896ff833df93389aec01768d40a39567f9abcce8f4318e8139e50e8726/retype-20.10.0.tar.gz
Summary  : re-apply types from .pyi stub files to your codebase
Group    : Development/Tools
License  : MIT
Requires: retype-bin = %{version}-%{release}
Requires: retype-license = %{version}-%{release}
Requires: retype-python = %{version}-%{release}
Requires: retype-python3 = %{version}-%{release}
Requires: click
Requires: pathspec
Requires: typed_ast
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : pathspec
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : typed_ast
BuildRequires : virtualenv

%description
[![Latest version on

%package bin
Summary: bin components for the retype package.
Group: Binaries
Requires: retype-license = %{version}-%{release}

%description bin
bin components for the retype package.


%package license
Summary: license components for the retype package.
Group: Default

%description license
license components for the retype package.


%package python
Summary: python components for the retype package.
Group: Default
Requires: retype-python3 = %{version}-%{release}

%description python
python components for the retype package.


%package python3
Summary: python3 components for the retype package.
Group: Default
Requires: python3-core
Provides: pypi(retype)
Requires: pypi(click)
Requires: pypi(pathspec)
Requires: pypi(typed_ast)

%description python3
python3 components for the retype package.


%prep
%setup -q -n retype-20.10.0
cd %{_builddir}/retype-20.10.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602522687
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/retype
cp %{_builddir}/retype-20.10.0/LICENSE %{buildroot}/usr/share/package-licenses/retype/f037b5ef1125b5a7f79d85910c7ae8ee6955df7b
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/retype

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/retype/f037b5ef1125b5a7f79d85910c7ae8ee6955df7b

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
