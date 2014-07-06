Configurar o tema a ser usado
-------------------------------------------------------------------------

Para configurar o tema a ser utilizado, basta alterar o arquivo xmlui.xconf file, na pasta config do Dspace.

Locate the <themes> block inside the xmlui.xconf and add an entry to your own theme there. The theme's location is specified by the path attribute while the set of DSpace pages it applies to can be specified in thee different ways:

With regex pattern: <theme name=" Theme's name" regex="community-list" path=" YourThemeDir /"/>
Directly with a handle: <theme name=" Theme's name" handle="123456789/42" path=" YourThemeDir /"/>
Or both: <theme name=" Theme's name" regex="browse-title^" handle="123456789/42" path=" YourThemeDir /"/>
