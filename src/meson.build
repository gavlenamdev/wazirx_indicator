pkgdatadir = join_paths(get_option('prefix'), get_option('datadir'), meson.project_name())
moduledir = join_paths(pkgdatadir, 'wazirx_indicator')
gnome = import('gnome')

gnome.compile_resources('wazirx_indicator',
  'wazirx_indicator.gresource.xml',
  gresource_bundle: true,
  install: true,
  install_dir: pkgdatadir,
)

python = import('python')

py_installation = python.find_installation('python3')
if not py_installation.found()
    error('No valid python3 binary found')
endif
if not py_installation.language_version().version_compare('>= 3.7')
  error('Python 3.7 or newer is required.')
endif


PROJECT_RDNN_NAME = 'org.github.gavlenamdev.wazirx_indicator'
APPLICATION_ID = 'org.github.gavlenamdev.wazirx_indicator'
PYTHON_DIR = py_installation.get_path('purelib')
# PYTHON_DIR = '/home/plugxr/Projects/wazirx_indicator/env3.9/lib/python3.9/site-packages'
PKGDATA_DIR = join_paths(get_option('prefix'), get_option('datadir'), APPLICATION_ID)
PKGLIB_DIR = join_paths(get_option('prefix'), get_option('libdir'), APPLICATION_ID)

# Dependencies
dependency('glib-2.0', version: '>= 2.67.1')
dependency('gobject-introspection-1.0', version: '>= 1.35.0')
dependency('gtk+-3.0', version: '>= 3.24.13')
dependency('libsoup-2.4')
dependency('pango', version: '>= 1.44.0')
dependency('pygobject-3.0', version: '>= 3.36.1')
dependency('py3cairo', version: '>= 1.14.0')
#dependency('appindicator', version: '>= 12.10.1')

#dependency('grilo-0.3', version: '>= 0.3.13', fallback: ['grilo', 'libgrl_dep'])
#dependency('grilo-plugins-0.3', version: '>= 0.3.12', fallback: ['grilo-plugins', 'grilo_plugins_dep'])


conf = configuration_data()
conf.set('application_id', APPLICATION_ID)
conf.set('rdnn_name', PROJECT_RDNN_NAME)
conf.set('pythondir', PYTHON_DIR)
conf.set('schemasdir', pkgdatadir)
conf.set('PYTHON', '/usr/bin/env python3')
conf.set('VERSION', meson.project_version())
conf.set('localedir', join_paths(get_option('prefix'), get_option('localedir')))
conf.set('pkgdatadir', pkgdatadir)

configure_file(
  input: 'wazirx_indicator.in',
  output: 'wazirx_indicator',
  configuration: conf,
  install: true,
  install_dir: get_option('bindir')
)

wazirx_indicator_sources = [
  '__init__.py',
  'main.py',
  'config.py',
  'home_window.py',
]

install_subdir('helpers', install_dir: moduledir)
install_subdir('widget', install_dir: moduledir)
install_subdir('models', install_dir: moduledir)
install_data(wazirx_indicator_sources, install_dir: moduledir)
