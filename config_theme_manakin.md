Configurar o tema a ser usado
-------------------------------------------------------------------------

Para configurar o tema a ser utilizado, basta alterar o arquivo xmlui.xconf file, na pasta config do Dspace.

Locate the <themes> block inside the xmlui.xconf and add an entry to your own theme there. The theme's location is specified by the path attribute while the set of DSpace pages it applies to can be specified in thee different ways:

With regex pattern: <theme name=" Theme's name" regex="community-list" path=" YourThemeDir /"/>
Directly with a handle: <theme name=" Theme's name" handle="123456789/42" path=" YourThemeDir /"/>
Or both: <theme name=" Theme's name" regex="browse-title^" handle="123456789/42" path=" YourThemeDir /"/>



-------------------------------------------------------------------------
Logo da página Dspace - Tema Mirage
-------------------------------------------------------------------------
Alteração do arquivo css 
[dspace]/webapps/xmlui/themes/Mirage/lib/css/style.css
de: dspace-logo-only.png para: logo_portal.gif

Alterar o texto "mirage" no arquivo
[dspace]/webapps/xmlui/themes/Mirage/lib/xsl/core/page-structure.xsl

-------------------------------------------------------------------------
Imagens estáticas
-------------------------------------------------------------------------
C:\dspace\webapps\xmlui\static\images


-------------------------------------------------------------------------
Alteração de busca do lado direito - Busca Por Autor e Titulo
-------------------------------------------------------------------------
No C:\dspace\config\dspace.cfg item 

###### Browse Configuration ######
webui.browse.index.1 = author:metadata:dc.creator:text
webui.browse.index.2 = title:item:title


-------------------------------------------------------------------------
Alteração de busca, remover acentuação quando fizer a busca
ex: historia e história geram resultados diferentes
-------------------------------------------------------------------------
No C:\dspace\config\dspace.cfg adicionar o analyser de busca abaixo
search.analyzer = org.apache.lucene.analysis.br.BrazilianAnalyzer
Após fazer isso, regerar os indices:> C:\Users\Rodrigo\Dropbox\bibliografia_infantil\uteis\reindex.bat

-------------------------------------------------------------------------
Exibir o logo da coleção, na listagem de coleções
-------------------------------------------------------------------------
no arquivo C:\dspace\webapps\xmlui\themes\custom-theme\lib\xsl\aspect\artifactbrowser\collection-list.xsl
Incluir dentro da tag <xsl:template name="collectionDetailList-DIM">:

<!-- Generate the logo, if present, from the file section -->
<xsl:apply-templates select="./mets:fileSec/mets:fileGrp[@USE='LOGO']"/>

-------------------------------------------------------------------------
Alteração da listagem de itens
-------------------------------------------------------------------------
no arquivo C:\dspace\webapps\xmlui\themes\custom-theme\lib\xsl\aspect\artifactbrowser\item-list.xsl



-------------------------------------------------------------------------
Remover a busca do menu lateral, alteração no arquivo navigation - cancelado, busca retornou ao local
conforme solicitação do cliente
-------------------------------------------------------------------------
no arquivo C:\dspace\webapps\xmlui\themes\custom-theme\lib\xsl\core\navigation.xsl


-------------------------------------------------------------------------
Alterar/Incluir Javascripts
-------------------------------------------------------------------------
no arquivo C:\dspace\webapps\xmlui\themes\custom-theme\lib\xsl\core\page-structure.xsl


-------------------------------------------------------------------------
Alterar página inicial - Página inicial do Dspace - Alteração/Customização
-------------------------------------------------------------------------
c:\dspace\config\news-xmlui.xml
-Por favor não esqueça de colocar Página em Desenvolvimento. Estará disponível até o final 
do segundo semestre de 2012.

-------------------------------------------------------------------------
Alterar ordenação de coleções por ordem de id decrescente
-------------------------------------------------------------------------
Alterar o arquivo C:\dspace1.8.0-src\dspace-api\src\main\java\org\dspace\content\Community.java
linha 624 - alterar para "AND community2collection.community_id= ? ORDER BY collection.name DESC",

- Após essa correção é necessário recompilar todo o dspace com o comando
c:\dspace-1.8.0-src\dspace mvn package

gerar o ant com as atualizações ant 
C:\dspace-1.8.2-src\dspace\target\dspace-1.8.0-build\ant update

Renomear os arquivos abaixo para os nomes originais

C:\dspace\config\
input-forms.xml-20120818-173637.old
item-submission.xml-20120818-173637
log4j.properties-20120818-173637.old
xmlui.xconf-20120818-173637.old para xmlui.xconf
news-xmlui.xml-20120818-173637.old
oaicat.properties-20120818-173637.old

-------------------------------------------------------------------------
Remover RSS 1.0 e Atom na página inicial - ok 22/09/2012
-------------------------------------------------------------------------
dspace.config
alterar linha 
webui.feed.formats = rss_1.0,rss_2.0,atom_1.0
para
webui.feed.formats = rss_2.0

-------------------------------------------------------------------------
Incluir o link no menu inicial para o curriculo dos resenhadores - 29/09/2012 - ok
-------------------------------------------------------------------------
no arquivo C:\dspace\webapps\xmlui\themes\custom-theme\lib\xsl\core\navigation.xsl


-------------------------------------------------------------------------
Incluir logos da SMC e do SMB no rodapé da página.
-------------------------------------------------------------------------
no arquivo C:\dspace\webapps\xmlui\themes\custom-theme\lib\xsl\core\page-structure.xsl
e no css

#ds-footer-logo-smb {
	display: inline-block;
	background: url('../../images/logo_smb.jpg');
	background-repeat: no-repeat;
	width: 79px;
	height: 60px;
}

#ds-footer-logo-smc {
	display: inline-block;
	background: url('../../images/logo_smc.jpg');
	background-repeat: no-repeat;
	width: 79px;
	height: 33px;
}


-------------------------------------------------------------------------
Incluir logo 4 elementos no rodapé da página.
-------------------------------------------------------------------------
no arquivo C:\dspace\webapps\xmlui\themes\custom-theme\lib\xsl\core\page-structure.xsl
e no css


-------------------------------------------------------------------------
Alterar a exibição de registro simples para que apareça todos os campos
de acordo com o formulário de inclusão
-------------------------------------------------------------------------
no arquivo C:\dspace\webapps\xmlui\themes\custom-theme\lib\xsl\aspect\artifactbrowser\item-view.xsl



-------------------------------------------------------------------------
Alterar a capa indisponivel do livro
-------------------------------------------------------------------------
no arquivo C:\dspace\webapps\xmlui\themes\custom-theme\lib\xsl\aspect\artifactbrowser\item-list.xsl

colocar a imagem estatica em 
\xmlui\static\images\capa_indisponivel.jpg

-------------------------------------------------------------------------
Alterar o link da página inicial Contexto -> Criar Volume para a Bibliografia
para apontar para criar uma nova coleção 
-------------------------------------------------------------------------
Arquivos:
C:\dspace\webapps\xmlui\themes\custom-theme\lib\xsl\core\page-structure.xsl
incluir javascript jquery

Incluir na linha 754

$("#aspect_viewArtifacts_Navigation_list_context a[href='/admin/community?createNew']").attr('href', 
'<xsl:text disable-output-escaping="yes">/admin/collection?createNew&amp;communityID=1</xsl:text>');
			
-------------------------------------------------------------------------
Alterar a porta do servidor Glassfish para a porta 80 e alterar para a 
raiz da aplicação
-------------------------------------------------------------------------
C:\Program Files\glassfish-3.1.2\glassfish\domains\domain1\config\domain.xml

And look for the network binds like the following:

<network-listeners>
<network-listener port=8080? protocol=http-listener-1? transport=tcp name=http-listener-1? thread-pool=http-thread-pool></network-listener>
<network-listener port=8181? protocol=http-listener-2? transport=tcp name=http-listener-2? thread-pool=http-thread-pool></network-listener>
<network-listener port=4848? protocol=admin-listener transport=tcp name=admin-listener thread-pool=admin-thread-pool></network-listener>
</network-listeners>

Then simply change them however you want, in my case I just changed the default listener on 8080 to 8082

<network-listeners>
<network-listener port=8082? protocol=http-listener-1? transport=tcp name=http-listener-1? thread-pool=http-thread-pool></network-listener>
<network-listener port=8181? protocol=http-listener-2? transport=tcp name=http-listener-2? thread-pool=http-thread-pool></network-listener>
<network-listener port=4848? protocol=admin-listener transport=tcp name=admin-listener thread-pool=admin-thread-pool></network-listener>
</network-listeners>

Very simple steps
Open (in notepad or other text editor) domain.xml located in /glassfish/domains/domain1/config folder.
Search for 8080 (there should be one occurance only ideally)
Change it to 80 or 8088 or 8090  whatever port no. you like and start the server.
There is no step 4 




-------------------------------------------------------------------------
Alterar a mensagem de e-mail workflow que estava desconfigurada
-------------------------------------------------------------------------
Alterado o arquivo Messages.properties localizado em 
c:\dspace-1.8.0-src\dspace-api\src\main\resources - linha 1444, 1445 e 1446

org.dspace.workflow.WorkflowManager.step1 = Requer revisão.
org.dspace.workflow.WorkflowManager.step2 = O depósito deve ser verificado antes de ser incluído no arquivo.
org.dspace.workflow.WorkflowManager.step3 = É necessário verificar os metadados para assegurar conformidade com os standards da coleção e editar, se necessário.

Salvar o arquivo como ANSI e recompilar o DSpace

c;\dspace=1.8.-src/dspace
mvn package

cd target\dspace1.8-build
ant update_code

-------------------------------------------------------------------------
Limitar a quantidade de caracteres no campo resenha - 800 caracteres
-------------------------------------------------------------------------
salva a biblioteca jquery jquery.limit-1.2.source.js e salva no
diretório \xmlui\themes\custom-theme\lib\js

incluída a biblioteca jquery na linha 143
no arquivo sitemap.xmap na pasta custom-theme

<!-- jquery limit -->
<map:parameter name="javascript#2" value="lib/js/jquery.limit-1.2.source.js"/>

incluído a linha abaixo no arquivo 
\Dropbox\bibliografia_infantil\xmlui\themes\custom-theme\lib\xsl\core
page-structure.xsl - linha 762
$('#aspect_submission_StepTransformer_field_dc_description_abstract').limit('800');



