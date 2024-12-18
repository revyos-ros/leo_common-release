%bcond_without tests
%bcond_without weak_deps

%global __os_install_post %(echo '%{__os_install_post}' | sed -e 's!/usr/lib[^[:space:]]*/brp-python-bytecompile[[:space:]].*$!!g')
%global __provides_exclude_from ^/opt/ros/jazzy/.*$
%global __requires_exclude_from ^/opt/ros/jazzy/.*$

Name:           ros-jazzy-leo-msgs
Version:        3.0.4
Release:        1%{?dist}%{?release_suffix}
Summary:        ROS leo_msgs package

License:        MIT
URL:            http://wiki.ros.org/leo
Source0:        %{name}-%{version}.tar.gz

Requires:       ros-jazzy-builtin-interfaces
Requires:       ros-jazzy-rosidl-default-runtime
Requires:       ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-ament-cmake
BuildRequires:  ros-jazzy-builtin-interfaces
BuildRequires:  ros-jazzy-rosidl-default-generators
BuildRequires:  ros-jazzy-ros-workspace
BuildRequires:  ros-jazzy-rosidl-typesupport-fastrtps-c
BuildRequires:  ros-jazzy-rosidl-typesupport-fastrtps-cpp
Provides:       %{name}-devel = %{version}-%{release}
Provides:       %{name}-doc = %{version}-%{release}
Provides:       %{name}-runtime = %{version}-%{release}
Provides:       ros-jazzy-rosidl-interface-packages(member)

%if 0%{?with_tests}
BuildRequires:  ros-jazzy-ament-cmake-lint-cmake
BuildRequires:  ros-jazzy-ament-cmake-xmllint
BuildRequires:  ros-jazzy-ament-lint-auto
%endif

%if 0%{?with_weak_deps}
Supplements:    ros-jazzy-rosidl-interface-packages(all)
%endif

%description
Message and Service definitions for Leo Rover

%prep
%autosetup -p1

%build
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
mkdir -p .obj-%{_target_platform} && cd .obj-%{_target_platform}
%cmake3 \
    -UINCLUDE_INSTALL_DIR \
    -ULIB_INSTALL_DIR \
    -USYSCONF_INSTALL_DIR \
    -USHARE_INSTALL_PREFIX \
    -ULIB_SUFFIX \
    -DCMAKE_INSTALL_PREFIX="/opt/ros/jazzy" \
    -DAMENT_PREFIX_PATH="/opt/ros/jazzy" \
    -DCMAKE_PREFIX_PATH="/opt/ros/jazzy" \
    -DSETUPTOOLS_DEB_LAYOUT=OFF \
%if !0%{?with_tests}
    -DBUILD_TESTING=OFF \
%endif
    ..

%make_build

%install
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
%make_install -C .obj-%{_target_platform}

%if 0%{?with_tests}
%check
# Look for a Makefile target with a name indicating that it runs tests
TEST_TARGET=$(%__make -qp -C .obj-%{_target_platform} | sed "s/^\(test\|check\):.*/\\1/;t f;d;:f;q0")
if [ -n "$TEST_TARGET" ]; then
# In case we're installing to a non-standard location, look for a setup.sh
# in the install tree and source it.  It will set things like
# CMAKE_PREFIX_PATH, PKG_CONFIG_PATH, and PYTHONPATH.
if [ -f "/opt/ros/jazzy/setup.sh" ]; then . "/opt/ros/jazzy/setup.sh"; fi
CTEST_OUTPUT_ON_FAILURE=1 \
    %make_build -C .obj-%{_target_platform} $TEST_TARGET || echo "RPM TESTS FAILED"
else echo "RPM TESTS SKIPPED"; fi
%endif

%files
/opt/ros/jazzy

%changelog
* Wed Dec 18 2024 Fictionlab <support@fictionlab.pl> - 3.0.4-1
- Autogenerated by Bloom

* Sun May 12 2024 Fictionlab <support@fictionlab.pl> - 3.0.3-1
- Autogenerated by Bloom

* Sat Apr 27 2024 Fictionlab <support@fictionlab.pl> - 3.0.2-1
- Autogenerated by Bloom

* Thu Apr 18 2024 Fictionlab <support@fictionlab.pl> - 3.0.1-3
- Autogenerated by Bloom

* Wed Mar 06 2024 Fictionlab <support@fictionlab.pl> - 3.0.1-2
- Autogenerated by Bloom

