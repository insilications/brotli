#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : brotli
Version  : 1.0.7
Release  : 8
URL      : https://github.com/google/brotli/archive/v1.0.7.tar.gz
Source0  : https://github.com/google/brotli/archive/v1.0.7.tar.gz
Summary  : Brotli encoder library
Group    : Development/Tools
License  : MIT
Requires: brotli-bin = %{version}-%{release}
Requires: brotli-lib = %{version}-%{release}
Requires: brotli-license = %{version}-%{release}
BuildRequires : buildreq-cmake
BuildRequires : buildreq-distutils3
BuildRequires : buildreq-golang
BuildRequires : cmake

%description
BROTLI DATA COMPRESSIOM LIBRARY
Brotli is a generic-purpose lossless compression algorithm that compresses data
using a combination of a modern variant of the LZ77 algorithm, Huffman coding
and 2nd order context modeling, with a compression ratio comparable to the best
currently available general-purpose compression methods. It is similar in speed
with deflate but offers more dense compression.

%package bin
Summary: bin components for the brotli package.
Group: Binaries
Requires: brotli-license = %{version}-%{release}

%description bin
bin components for the brotli package.


%package dev
Summary: dev components for the brotli package.
Group: Development
Requires: brotli-lib = %{version}-%{release}
Requires: brotli-bin = %{version}-%{release}
Provides: brotli-devel = %{version}-%{release}

%description dev
dev components for the brotli package.


%package lib
Summary: lib components for the brotli package.
Group: Libraries
Requires: brotli-license = %{version}-%{release}

%description lib
lib components for the brotli package.


%package license
Summary: license components for the brotli package.
Group: Default

%description license
license components for the brotli package.


%prep
%setup -q -n brotli-1.0.7

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1540748555
mkdir -p clr-build
pushd clr-build
%cmake ..
make  %{?_smp_mflags} VERBOSE=1
popd

%install
export SOURCE_DATE_EPOCH=1540748555
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/brotli
cp LICENSE %{buildroot}/usr/share/package-licenses/brotli/LICENSE
pushd clr-build
%make_install
popd

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/brotli

%files dev
%defattr(-,root,root,-)
/usr/include/brotli/decode.h
/usr/include/brotli/encode.h
/usr/include/brotli/port.h
/usr/include/brotli/types.h
/usr/lib64/libbrotlicommon.so
/usr/lib64/libbrotlidec.so
/usr/lib64/libbrotlienc.so
/usr/lib64/pkgconfig/libbrotlicommon.pc
/usr/lib64/pkgconfig/libbrotlidec.pc
/usr/lib64/pkgconfig/libbrotlienc.pc

%files lib
%defattr(-,root,root,-)
/usr/lib64/libbrotlicommon.so.1
/usr/lib64/libbrotlicommon.so.1.0.7
/usr/lib64/libbrotlidec.so.1
/usr/lib64/libbrotlidec.so.1.0.7
/usr/lib64/libbrotlienc.so.1
/usr/lib64/libbrotlienc.so.1.0.7

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/brotli/LICENSE
