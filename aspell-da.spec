%define _enable_debug_packages %{nil}
%define debug_package          %{nil}

%define src_ver 1.6.16
%define fname new_aspell-da
%define aspell_ver 0.60
%define languagelocal dansk
%define languageeng danish
%define languageenglazy Danish
%define languagecode da

Summary:       %{languageenglazy} files for aspell
Name:          aspell-%{languagecode}
Version:       1.6.16
Release:       %mkrel 1
Epoch:	       1
Group:         System/Internationalization
Source:        http://da.speling.org/filer/new_aspell-da-%version.tar.bz2
URL:           http://da.speling.org/
License:       GPL
BuildRoot:     %{_tmppath}/%{name}-%{version}-root
Provides: spell-da

BuildRequires: aspell >= %{aspell_ver}
Requires:      aspell >= %{aspell_ver}

# Mandriva Stuff
Requires:      locales-%{languagecode}
# aspell = 1, myspell = 2, lang-specific = 3
Provides:      enchant-dictionary = 1
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
%doc README*
%{_libdir}/aspell-%{aspell_ver}/*


