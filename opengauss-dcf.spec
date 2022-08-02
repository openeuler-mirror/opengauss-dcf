Name:             DCF
Version:          1.0.0
Release:          3
Summary:          A distributed consensus framework library
License:          MulanPSL-2.0
URL:              https://gitee.com/opengauss/DCF
Source0:          %{name}-%{version}.tar.gz

Patch1:           01-boundcheck.patch
Patch2:           DCF-1.0.0-sw.patch

BuildRequires: cmake gcc gcc-c++ lz4-devel openssl-devel zstd-devel libboundscheck cjson-devel


%description
DCF is A distributed consensus framework library for openGauss


%prep
%setup -q
%patch1 -p1
%ifarch sw_64
%patch2 -p1
%endif

%build
cmake -DCMAKE_BUILD_TYPE=Release -DUSE32BIT=OFF -DTEST=OFF -DENABLE_EXPORT_API=OFF CMakeLists.txt
%make_build all -s %{?_smp_mflags}


%install
mkdir -p %{buildroot}/%{_prefix}/include
mkdir -p %{buildroot}/%{_prefix}/lib64
cp src/interface/dcf_interface.h %{buildroot}/%{_prefix}/include
cp output/lib/libdcf.* %{buildroot}/%{_prefix}/lib64

%post

%preun

%files
%defattr (-,root,root)
%{_prefix}/include/dcf_interface.h
%{_prefix}/lib64/libdcf.so

%changelog
* Thu Jul 28 2022 wuzx<wuzx1226@qq.com> - 1.0.0-3
- add sw64 patch

* Thu Feb 10 2022 zhangxubo <zhangxubo1@huawei.com> - 1.0.0-2
- #I4T3R3 move library file to /usr/lib64 path.

* Wed Dec 1 2021 zhangxubo <zhangxubo1@huawei.com> - 1.0.0-1
- Package init
