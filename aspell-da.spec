%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.4.42-1
%define fname aspell5-%{languagecode}
%define aspell_ver 0.60
%define languagelocal dansk
%define languageeng danish
%define languageenglazy Danish
%define languagecode da

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       1.4.42.1
Release:       %mkrel 4
Epoch:	       1
Group:         System/Internationalization
Source:        http://ftp.gnu.org/gnu/aspell/dict/%{languagecode}/%{fname}-%{src_ver}.tar.bz2
URL:           http://aspell.sourceforge.net/
License:       GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-da

BuildRequires: aspell >= %{aspell_ver}
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
Provides:      aspell-dictionary aspell-dk

# RedHat Stuff.
#Obsoletes: ispell-dk, ispell-danish
Obsoletes: aspell-dk

Autoreqprov:   no

%description
A %{languageenglazy} dictionary for use with aspell, a spelling checker.

%prep
%setup -q -n %{fname}-%{src_ver}

%build

# don't use configure macro
./configure

%make

%install
rm -fr $RPM_BUILD_ROOT

%makeinstall_std

chmod 644 README Copyright

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README* Copyright doc/contributors
%{_libdir}/aspell-%{aspell_ver}/*


