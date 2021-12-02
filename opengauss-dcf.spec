Name:             DCF
Version:          1.0.0
Release:          1
Summary:          A distributed consensus framework library
License:          MulanPSL-2.0
URL:              https://gitee.com/opengauss/DCF
Source0:          %{name}-%{version}.tar.gz

Patch1:           01-boundcheck.patch

BuildRequires: cmake gcc gcc-c++ lz4-devel openssl-devel zstd-devel libboundscheck cjson-devel


%description
DCF is A distributed consensus framework library for openGauss


%prep
%setup -q
%patch1 -p1

%build
cmake -DCMAKE_BUILD_TYPE=Release -DUSE32BIT=OFF -DTEST=OFF -DENABLE_EXPORT_API=OFF CMakeLists.txt
%make_build all -s %{?_smp_mflags}


%install
mkdir -p %{buildroot}/%{_prefix}/include
mkdir -p %{buildroot}/%{_prefix}/lib
cp src/interface/dcf_interface.h %{buildroot}/%{_prefix}/include
cp output/lib/libdcf.* %{buildroot}/%{_prefix}/lib

%post

%preun

%files
%defattr (-,root,root)
%{_prefix}/include/dcf_interface.h
%{_prefix}/lib/libdcf.so

%changelog
* Wed Dec 1 2021 zhangxubo <zhangxubo1@huawei.com> - 1.0.0-1
- Package init