#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0xB26995E310250568 (lukasz@python.org)
#
Name     : retype
Version  : 17.12.0
Release  : 14
URL      : https://files.pythonhosted.org/packages/6e/da/ca9f5560f051d2ed79a52de1170903e3ff8ad011cff56c65abfcff38d372/retype-17.12.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/6e/da/ca9f5560f051d2ed79a52de1170903e3ff8ad011cff56c65abfcff38d372/retype-17.12.0.tar.gz
Source99 : https://files.pythonhosted.org/packages/6e/da/ca9f5560f051d2ed79a52de1170903e3ff8ad011cff56c65abfcff38d372/retype-17.12.0.tar.gz.asc
Summary  : Re-apply types from .pyi stub files to your codebase.
Group    : Development/Tools
License  : MIT
Requires: retype-bin
Requires: retype-python3
Requires: retype-python
Requires: click
Requires: typed-ast
BuildRequires : buildreq-distutils3
BuildRequires : click
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python3-dev
BuildRequires : setuptools
BuildRequires : typed-ast

%description
======
        
        |Build Status|
        
        Re-apply type annotations from .pyi stubs to your codebase.
        
        Usage
        -----

%package bin
Summary: bin components for the retype package.
Group: Binaries

%description bin
bin components for the retype package.


%package python
Summary: python components for the retype package.
Group: Default
Requires: retype-python3

%description python
python components for the retype package.


%package python3
Summary: python3 components for the retype package.
Group: Default
Requires: python3-core

%description python3
python3 components for the retype package.


%prep
%setup -q -n retype-17.12.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1532307578
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.7/site-packages python3 setup.py test
%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)
/usr/lib/mypy/typeshed/third_party/3.6/retype.pyi
/usr/lib/mypy/typeshed/third_party/3.6/retype_hgext.pyi

%files bin
%defattr(-,root,root,-)
/usr/bin/retype

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
