#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : mvn-animal-sniffer
Version  : 1.15
Release  : 1
URL      : https://repo1.maven.org/maven2/org/codehaus/mojo/animal-sniffer/1.15/animal-sniffer-1.15.jar
Source0  : https://repo1.maven.org/maven2/org/codehaus/mojo/animal-sniffer/1.15/animal-sniffer-1.15.jar
Source1  : https://repo1.maven.org/maven2/org/codehaus/mojo/animal-sniffer-annotations/1.14/animal-sniffer-annotations-1.14.jar
Source2  : https://repo1.maven.org/maven2/org/codehaus/mojo/animal-sniffer-annotations/1.14/animal-sniffer-annotations-1.14.pom
Source3  : https://repo1.maven.org/maven2/org/codehaus/mojo/animal-sniffer-maven-plugin/1.15/animal-sniffer-maven-plugin-1.15.jar
Source4  : https://repo1.maven.org/maven2/org/codehaus/mojo/animal-sniffer-maven-plugin/1.15/animal-sniffer-maven-plugin-1.15.pom
Source5  : https://repo1.maven.org/maven2/org/codehaus/mojo/animal-sniffer-parent/1.14/animal-sniffer-parent-1.14.pom
Source6  : https://repo1.maven.org/maven2/org/codehaus/mojo/animal-sniffer-parent/1.15/animal-sniffer-parent-1.15.pom
Source7  : https://repo1.maven.org/maven2/org/codehaus/mojo/animal-sniffer/1.15/animal-sniffer-1.15.pom
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: mvn-animal-sniffer-data = %{version}-%{release}

%description
No detailed description available

%package data
Summary: data components for the mvn-animal-sniffer package.
Group: Data

%description data
data components for the mvn-animal-sniffer package.


%prep

%build

%install
mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer/1.15
cp %{SOURCE0} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer/1.15

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer/1.15
cp %{SOURCE1} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer/1.15

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-annotations/1.14
cp %{SOURCE2} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-annotations/1.14

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-annotations/1.14
cp %{SOURCE3} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-annotations/1.14

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-maven-plugin/1.15
cp %{SOURCE4} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-maven-plugin/1.15

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-maven-plugin/1.15
cp %{SOURCE5} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-maven-plugin/1.15

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-parent/1.14
cp %{SOURCE6} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-parent/1.14

mkdir -p %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-parent/1.15
cp %{SOURCE7} %{buildroot}/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-parent/1.15


%files
%defattr(-,root,root,-)

%files data
%defattr(-,root,root,-)
/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-annotations/1.14/animal-sniffer-annotations-1.14.pom
/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-annotations/1.14/animal-sniffer-maven-plugin-1.15.jar
/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-maven-plugin/1.15/animal-sniffer-maven-plugin-1.15.pom
/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-maven-plugin/1.15/animal-sniffer-parent-1.14.pom
/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-parent/1.14/animal-sniffer-parent-1.15.pom
/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer-parent/1.15/animal-sniffer-1.15.pom
/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer/1.15/animal-sniffer-1.15.jar
/usr/share/java/.m2/repository/org/codehaus/mojo/animal-sniffer/1.15/animal-sniffer-annotations-1.14.jar
