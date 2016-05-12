http://wiki.lib.sun.ac.za/index.php/SUNScholar/Search_Indexes#Check_Config

Check Config
------------

Para checar sua configuração, roda o seguinte comando:

```sh
sudo /dspace/bin/dspace dsrun org.dspace.discovery.configuration.DiscoveryConfigurationService
```

Veja um exemplo abaixo da saída do comando:

```code
79
default
Facets:
	advisor
		dc.contributor.advisor
	author
		dc.contributor.author
		dc.creator
	subject
		dc.subject.*
	dateIssued
		dc.date.issued
Search filters
		dc.title
		dc.contributor.advisor
		dc.contributor.author
		dc.creator
		dc.subject.*
		dc.date.issued
		dc.type
		dc.description.provenance
Recent submissions configuration:
	Metadata sort field: dc.date.accessioned
	Max recent submissions: 30
site
Facets:
	advisor
		dc.contributor.advisor
	author
		dc.contributor.author
		dc.creator
	subject
		dc.subject.*
	dateIssued
		dc.date.issued
Search filters
		dc.title
		dc.contributor.advisor
		dc.contributor.author
		dc.creator
		dc.subject.*
		dc.date.issued
		dc.type
		dc.description.provenance
Recent submissions configuration:
	Metadata sort field: dc.date.accessioned
	Max recent submissions: 30
```code	
	
http://wiki.lib.sun.ac.za/index.php/SUNScholar/Discovery/5.X
	
Step 1 - Define Discovery SOLR service
Edit the following file:

nano $HOME/source/dspace/config/modules/discovery.cfg
See example below.

#---------------------------------------------------------------#
#-----------------DISCOVERY CONFIGURATIONS----------------------#
#---------------------------------------------------------------#
# Configuration properties used solely by the Discovery         #
# faceted-search system.                                        #
#---------------------------------------------------------------#
##### Search Indexing #####
search.server = ${solr.server}/search

#Enable the url validation of the search.server setting above.
#Defaults to true: validation is enabled
#solr.url.validation.enabled = true

#Char used to ensure that the sidebar facets are case insensitive
#solr.facets.split.char=\n|||\n

# index.ignore-variants = false
# index.ignore-authority = false
index.projection=dc.title,dc.contributor.*,dc.date.issued

# ONLY-FOR-JSPUI: 
# 1) you need to set the DiscoverySearchRequestProcessor in the dspace.cfg 
# 2) to show facet on Site/Community/etc. you need to add a Site/Community/Collection
#	 Processors plugin in the dspace.cfg
Step 2 - Enable Discovery in XMLUI
Enable discovery by following: https://wiki.duraspace.org/display/DSDOC5x/Discovery#Discovery-EnablingDiscovery

Step 3 - Discovery Configuration
Edit the following file:

nano $HOME/source/dspace/config/spring/api/discovery.xml
Please note: All the sidebar facets MUST be a part of the search filters list

In the customised example below, "Advisor", "Type" and "Provenance" search fields have been added and "Provenance" has been removed from ignored metadata fields.

<?xml version="1.0" encoding="UTF-8"?>
<!--

    The contents of this file are subject to the license and copyright
    detailed in the LICENSE and NOTICE files at the root of the source
    tree and available online at

    http://www.dspace.org/license/

-->
<beans xmlns="http://www.springframework.org/schema/beans"
       xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
       xmlns:context="http://www.springframework.org/schema/context"
       xmlns:util="http://www.springframework.org/schema/util"
       xsi:schemaLocation="http://www.springframework.org/schema/beans
           http://www.springframework.org/schema/beans/spring-beans-3.0.xsd
           http://www.springframework.org/schema/context
           http://www.springframework.org/schema/context/spring-context-3.0.xsd
           http://www.springframework.org/schema/util
           http://www.springframework.org/schema/util/spring-util-3.0.xsd"
    default-autowire-candidates="*Service,*DAO,javax.sql.DataSource">

    <context:annotation-config /> <!-- allows us to use spring annotations in beans -->

    <bean id="solrServiceResourceIndexPlugin" class="org.dspace.discovery.SolrServiceResourceRestrictionPlugin" scope="prototype"/>
    <bean id="SolrServiceSpellIndexingPlugin" class="org.dspace.discovery.SolrServiceSpellIndexingPlugin" scope="prototype"/>

    <alias name="solrServiceResourceIndexPlugin" alias="org.dspace.discovery.SolrServiceResourceRestrictionPlugin"/>

    <!-- Additional indexing plugin to implement the browse system via SOLR -->
    <bean id="solrBrowseIndexer" scope="prototype"
          class="org.dspace.browse.SolrBrowseCreateDAO">
    </bean>

    <!--Bean that is used for mapping communities/collections to certain discovery configurations.-->
    <bean id="org.dspace.discovery.configuration.DiscoveryConfigurationService" class="org.dspace.discovery.configuration.DiscoveryConfigurationService">
        <property name="map">
            <map>
                <!--The map containing all the settings,
                    the key is used to refer to the page (the "site" or a community/collection handle)
                    the value-ref is a reference to an identifier of the DiscoveryConfiguration format
                    -->
                <!--The default entry, DO NOT REMOVE the system requires this-->
               <entry key="default" value-ref="defaultConfiguration" />

               <!--Use site to override the default configuration for the home page & default discovery page-->
               <entry key="site" value-ref="homepageConfiguration" />
               <!--<entry key="123456789/7621" value-ref="defaultConfiguration"/>-->
            </map>
        </property>
        <property name="toIgnoreMetadataFields">
            <map>
                <entry>
                    <key><util:constant static-field="org.dspace.core.Constants.COMMUNITY"/></key>
                    <list>
                        <!--Introduction text-->
                        <!--<value>dc.description</value>-->
                        <!--Short description-->
                        <!--<value>dc.description.abstract</value>-->
                        <!--News-->
                        <!--<value>dc.description.tableofcontents</value>-->
                        <!--Copyright text-->
                        <value>dc.rights</value>
                        <!--Community name-->
                        <!--<value>dc.title</value>-->
                    </list>
                </entry>
                <entry>
                    <key><util:constant static-field="org.dspace.core.Constants.COLLECTION"/></key>
                    <list>
                        <!--Introduction text-->
                        <!--<value>dc.description</value>-->
                        <!--Short description-->
                        <!--<value>dc.description.abstract</value>-->
                        <!--News-->
                        <!--<value>dc.description.tableofcontents</value>-->
                        <!--Copyright text-->
                        <value>dc.rights</value>
                        <!--Collection name-->
                        <!--<value>dc.title</value>-->
                    </list>
                </entry>
                <entry>
                    <key><util:constant static-field="org.dspace.core.Constants.ITEM"/></key>
                    <list>
                        <!-- <value>dc.description.provenance</value> -->
                    </list>
                </entry>
            </map>
        </property>
    </bean>

    <!--The default configuration settings for discovery-->
    <bean id="defaultConfiguration" class="org.dspace.discovery.configuration.DiscoveryConfiguration" scope="prototype">
        <!--Which sidebar facets are to be displayed-->
        <property name="sidebarFacets">
            <list>
                <ref bean="searchFilterAdvisor" />
                <ref bean="searchFilterAuthor" />
                <ref bean="searchFilterSubject" />
                <ref bean="searchFilterIssued" />
            </list>
        </property>
        <!-- Set TagCloud configuration per discovery configuration -->
        <property name="tagCloudFacetConfiguration" ref="defaultTagCloudFacetConfiguration"/>
        <!--The search filters which can be used on the discovery search page-->
        <property name="searchFilters">
            <list>
                <ref bean="searchFilterTitle" />
                <ref bean="searchFilterAdvisor" />
                <ref bean="searchFilterAuthor" />
                <ref bean="searchFilterSubject" />
                <ref bean="searchFilterIssued" />
                <ref bean="searchFilterType" />
                <ref bean="searchFilterProvenance" />
            </list>
        </property>
        <!--The sort filters for the discovery search-->
        <property name="searchSortConfiguration">
            <bean class="org.dspace.discovery.configuration.DiscoverySortConfiguration">
                <!--<property name="defaultSort" ref="sortDateIssued"/>-->
                <!--DefaultSortOrder can either be desc or asc (desc is default)-->
                <property name="defaultSortOrder" value="desc"/>
                <property name="sortFields">
                    <list>
                        <ref bean="sortTitle" />
                        <ref bean="sortDateIssued" />
                    </list>
                </property>
            </bean>
        </property>
        <!--Any default filter queries, these filter queries will be used for all queries done by discovery for this configuration-->
        <!--<property name="defaultFilterQueries">-->
            <!--<list>-->
                <!--Only find items-->
                <!--<value>search.resourcetype:2</value>-->
            <!--</list>-->
        <!--</property>-->
        <!--The configuration for the recent submissions-->
        <property name="recentSubmissionConfiguration">
            <bean class="org.dspace.discovery.configuration.DiscoveryRecentSubmissionsConfiguration">
                <property name="metadataSortField" value="dc.date.accessioned" />
                <property name="type" value="date"/>
                <property name="max" value="30"/>
                <!-- If enabled the collection home page will not display metadata but show a pageable list of recent submissions -->
                <property name="useAsHomePage" value="false"/>
            </bean>
        </property>
        <!--Default result per page  -->
        <property name="defaultRpp" value="30" />
        <property name="hitHighlightingConfiguration">
            <bean class="org.dspace.discovery.configuration.DiscoveryHitHighlightingConfiguration">
                <property name="metadataFields">
                    <list>
                        <bean class="org.dspace.discovery.configuration.DiscoveryHitHighlightFieldConfiguration">
                            <property name="field" value="dc.title"/>
                            <property name="snippets" value="20"/>
                        </bean>
                        <bean class="org.dspace.discovery.configuration.DiscoveryHitHighlightFieldConfiguration">
                            <property name="field" value="dc.contributor.author"/>
                            <property name="snippets" value="20"/>
                        </bean>
                        <bean class="org.dspace.discovery.configuration.DiscoveryHitHighlightFieldConfiguration">
                            <property name="field" value="dc.contributor.advisor"/>
                            <property name="snippets" value="20"/>
                        </bean>
                        <bean class="org.dspace.discovery.configuration.DiscoveryHitHighlightFieldConfiguration">
                            <property name="field" value="dc.description.abstract"/>
                            <property name="maxSize" value="250"/>
                            <property name="snippets" value="10"/>
                        </bean>
                        <bean class="org.dspace.discovery.configuration.DiscoveryHitHighlightFieldConfiguration">
                            <property name="field" value="fulltext"/>
                            <property name="maxSize" value="250"/>
                            <property name="snippets" value="10"/>
                        </bean>
                    </list>
                </property>
            </bean>
        </property>
        <property name="moreLikeThisConfiguration">
            <bean class="org.dspace.discovery.configuration.DiscoveryMoreLikeThisConfiguration">
                <!--When altering this list also alter the "xmlui.Discovery.RelatedItems.help" key as it describes
                the metadata fields below-->
                <property name="similarityMetadataFields">
                    <list>
                        <value>dc.title</value>
                        <value>dc.contributor.author</value>
        	    	    <value>dc.contributor.advisor</value>
                        <value>dc.creator</value>
                        <value>dc.subject</value>
                    </list>
                </property>
                <!--The minimum number of matching terms across the metadata fields above before an item is found as related -->
                <property name="minTermFrequency" value="5"/>
                <!--The maximum number of related items displayed-->
                <property name="max" value="20"/>
                <!--The minimum word length below which words will be ignored-->
                <property name="minWordLength" value="5"/>
            </bean>
        </property>
        <!-- When true a "did you mean" example will be displayed, value can be true or false -->
        <property name="spellCheckEnabled" value="true"/>
    </bean>


    <!--The Homepage specific configuration settings for discovery-->
    <bean id="homepageConfiguration" class="org.dspace.discovery.configuration.DiscoveryConfiguration" scope="prototype">
        <!--Which sidebar facets are to be displayed (same as defaultConfiguration above)-->
        <property name="sidebarFacets">
            <list>
                <ref bean="searchFilterAdvisor" />
                <ref bean="searchFilterAuthor" />
                <ref bean="searchFilterSubject" />
                <ref bean="searchFilterIssued" />
            </list>
        </property>
        <!-- Set TagCloud configuration per discovery configuration -->
        <property name="tagCloudFacetConfiguration" ref="homepageTagCloudFacetConfiguration"/>
        <!--The search filters which can be used on the discovery search page (same as defaultConfiguration above)-->
        <property name="searchFilters">
            <list>
                <ref bean="searchFilterTitle" />
                <ref bean="searchFilterAdvisor" />
                <ref bean="searchFilterAuthor" />
                <ref bean="searchFilterSubject" />
                <ref bean="searchFilterIssued" />
                <ref bean="searchFilterType" />
                <ref bean="searchFilterProvenance" />
            </list>
        </property>
        <!--The sort filters for the discovery search (same as defaultConfiguration above)-->
        <property name="searchSortConfiguration">
            <bean class="org.dspace.discovery.configuration.DiscoverySortConfiguration">
                <!--<property name="defaultSort" ref="sortDateIssued"/>-->
                <!--DefaultSortOrder can either be desc or asc (desc is default)-->
                <property name="defaultSortOrder" value="desc"/>
                <property name="sortFields">
                    <list>
                        <ref bean="sortTitle" />
                        <ref bean="sortDateIssued" />
                    </list>
                </property>
            </bean>
        </property>
        <!-- Limit recent submissions on homepage to only 5 (default is 20) -->
        <property name="recentSubmissionConfiguration">
            <bean class="org.dspace.discovery.configuration.DiscoveryRecentSubmissionsConfiguration">
                <property name="metadataSortField" value="dc.date.accessioned" />
                <property name="type" value="date"/>
                <property name="max" value="30"/>
                <property name="useAsHomePage" value="false"/>
            </bean>
        </property>
        <property name="hitHighlightingConfiguration">
            <bean class="org.dspace.discovery.configuration.DiscoveryHitHighlightingConfiguration">
                <property name="metadataFields">
                    <list>
                        <bean class="org.dspace.discovery.configuration.DiscoveryHitHighlightFieldConfiguration">
                            <property name="field" value="dc.title"/>
                            <property name="snippets" value="20"/>
                        </bean>
                        <bean class="org.dspace.discovery.configuration.DiscoveryHitHighlightFieldConfiguration">
                            <property name="field" value="dc.contributor.author"/>
                            <property name="snippets" value="20"/>
                        </bean>
                        <bean class="org.dspace.discovery.configuration.DiscoveryHitHighlightFieldConfiguration">
                            <property name="field" value="dc.description.abstract"/>
                            <property name="maxSize" value="250"/>
                            <property name="snippets" value="20"/>
                        </bean>
                        <bean class="org.dspace.discovery.configuration.DiscoveryHitHighlightFieldConfiguration">
                            <property name="field" value="fulltext"/>
                            <property name="maxSize" value="250"/>
                            <property name="snippets" value="20"/>
                        </bean>
                    </list>
                </property>
            </bean>
        </property>
        <!-- When true a "did you mean" example will be displayed, value can be true or false -->
        <property name="spellCheckEnabled" value="true"/>
    </bean>

    <!--TagCloud configuration bean for homepage discovery configuration-->
    <bean id="homepageTagCloudFacetConfiguration" class="org.dspace.discovery.configuration.TagCloudFacetConfiguration">
        <!-- Actual configuration of the tagcloud (colors, sorting, etc.) -->
        <property name="tagCloudConfiguration" ref="tagCloudConfiguration"/>
        <!-- List of tagclouds to appear, one for every search filter, one after the other -->
        <property name="tagCloudFacets">
            <list>
                <ref bean="searchFilterSubject" />
            </list>
        </property>
    </bean>
    
     <!--TagCloud configuration bean for default discovery configuration-->
    <bean id="defaultTagCloudFacetConfiguration" class="org.dspace.discovery.configuration.TagCloudFacetConfiguration">
        <!-- Actual configuration of the tagcloud (colors, sorting, etc.) -->
        <property name="tagCloudConfiguration" ref="tagCloudConfiguration"/>
        <!-- List of tagclouds to appear, one for every search filter, one after the other -->
        <property name="tagCloudFacets">
            <list>
                <ref bean="searchFilterSubject" />
            </list>
        </property>
    </bean>
    
    <bean id="tagCloudConfiguration" class="org.dspace.discovery.configuration.TagCloudConfiguration">
		<!-- Should display the score of each tag next to it? Default: false -->
		<!-- <property name="displayScore" value="true"/> -->
		
		<!-- Should display the tag as center aligned in the page or left aligned? Possible values: true | false. Default: true  -->
		<!-- <property name="shouldCenter" value="true"/> -->
		
		<!-- How many tags will be shown. Value -1 means all of them. Default: -1 -->
		<!--<property name="totalTags" value="-1"/> -->
		
		<!-- The letter case of the tags. 
			 Possible values: Case.LOWER | Case.UPPER | Case.CAPITALIZATION | Case.PRESERVE_CASE | Case.CASE_SENSITIVE
			 Default: Case.PRESERVE_CASE -->
		<!--<property name="cloudCase" value="Case.PRESERVE_CASE"/> -->
		
		<!-- If the 3 colors of the tag cloud should be independent of score (random=yes) or based on the score. Possible values: true | false . Default: true-->
		<!-- <property name="randomColors" value="true"/> -->

		<!-- The font size (in em) for the tag with the lowest score. Possible values: any decimal. Default: 1.1 -->
		<!-- <property name="fontFrom" value="1.1"/>-->
		
		<!-- The font size (in em) for the tag with the lowest score. Possible values: any decimal. Default: 3.2 -->
		<!-- <property name="fontTo" value="3.2"/>-->
		
		<!-- The score that tags with lower than that will not appear in the rag cloud. Possible values: any integer from 1 to infinity. Default: 0 -->
		<!-- <property name="cuttingLevel" value="0"/>-->

		<!-- The ordering of the tags (based either on the name or the score of the tag)
			 Possible values: Tag.NameComparatorAsc | Tag.NameComparatorDesc | Tag.ScoreComparatorAsc | Tag.ScoreComparatorDesc
			 Default: Tag.NameComparatorAsc  -->
		<!-- <property name="ordering" value="Tag.NameComparatorAsc"/>-->	
    </bean>
    
    <!-- The tag cloud parameters for the tag clouds that appear in the browse pages -->
    <bean id="browseTagCloudConfiguration" class="org.dspace.discovery.configuration.TagCloudConfiguration">
		<!-- Should display the score of each tag next to it? Default: false -->
		<!-- <property name="displayScore" value="true"/> -->
		
		<!-- Should display the tag as center aligned in the page or left aligned? Possible values: true | false. Default: true  -->
		<!-- <property name="shouldCenter" value="true"/> -->
		
		<!-- How many tags will be shown. Value -1 means all of them. Default: -1 -->
		<!--<property name="totalTags" value="-1"/> -->
		
		<!-- The letter case of the tags. 
			 Possible values: Case.LOWER | Case.UPPER | Case.CAPITALIZATION | Case.PRESERVE_CASE | Case.CASE_SENSITIVE
			 Default: Case.PRESERVE_CASE -->
		<!--<property name="cloudCase" value="Case.PRESERVE_CASE"/> -->
		
		<!-- If the 3 colors of the tag cloud should be independent of score (random=yes) or based on the score. Possible values: true | false . Default: true-->
		<!-- <property name="randomColors" value="true"/> -->

		<!-- The font size (in em) for the tag with the lowest score. Possible values: any decimal. Default: 1.1 -->
		<!-- <property name="fontFrom" value="1.1"/>-->
		
		<!-- The font size (in em) for the tag with the lowest score. Possible values: any decimal. Default: 3.2 -->
		<!-- <property name="fontTo" value="3.2"/>-->
		
		<!-- The tags with score lower than this will not appear in the tag cloud. Possible values: any integer from 1 to infinity. Default: 0 -->
		<!-- <property name="cuttingLevel" value="0"/>-->
	
		<!-- The ordering of the tags (based either on the name or the score of the tag)
			 Possible values: Tag.NameComparatorAsc | Tag.NameComparatorDesc | Tag.ScoreComparatorAsc | Tag.ScoreComparatorDesc
			 Default: Tag.NameComparatorAsc  -->
		<!-- <property name="ordering" value="Tag.NameComparatorAsc"/>-->	
    </bean>
    
    <!--Search filter configuration beans-->
    <bean id="searchFilterTitle" class="org.dspace.discovery.configuration.DiscoverySearchFilter">
        <property name="indexFieldName" value="title"/>
        <property name="metadataFields">
            <list>
                <value>dc.title</value>
            </list>
        </property>
    </bean>

    <bean id="searchFilterAuthor" class="org.dspace.discovery.configuration.DiscoverySearchFilterFacet">
        <property name="indexFieldName" value="author"/>
        <property name="metadataFields">
            <list>
                <value>dc.contributor.author</value>
                <value>dc.creator</value>
            </list>
        </property>
        <property name="facetLimit" value="30"/>
        <property name="sortOrder" value="COUNT"/>
    </bean>

    <bean id="searchFilterAdvisor" class="org.dspace.discovery.configuration.DiscoverySearchFilterFacet">
        <property name="indexFieldName" value="advisor"/>
        <property name="metadataFields">
            <list>
                <value>dc.contributor.advisor</value>
            </list>
        </property>
        <property name="facetLimit" value="30"/>
        <property name="sortOrder" value="COUNT"/>
    </bean>

    <bean id="searchFilterSubject" class="org.dspace.discovery.configuration.HierarchicalSidebarFacetConfiguration">
        <property name="indexFieldName" value="subject"/>
        <property name="metadataFields">
            <list>
                <value>dc.subject.*</value>
            </list>
        </property>
        <property name="facetLimit" value="30"/>
        <property name="sortOrder" value="COUNT"/>
        <property name="splitter" value="::"/>
    </bean>

    <bean id="searchFilterIssued" class="org.dspace.discovery.configuration.DiscoverySearchFilterFacet">
        <property name="indexFieldName" value="dateIssued"/>
        <property name="metadataFields">
            <list>
                <value>dc.date.issued</value>
            </list>
        </property>
        <property name="type" value="date"/>
        <property name="sortOrder" value="VALUE"/>
    </bean>

    <bean id="searchFilterType" class="org.dspace.discovery.configuration.DiscoverySearchFilter">
        <property name="indexFieldName" value="type"/>
        <property name="metadataFields">
            <list>
                <value>dc.type</value>
            </list>
        </property>
    </bean>

    <bean id="searchFilterProvenance" class="org.dspace.discovery.configuration.DiscoverySearchFilter">
        <property name="indexFieldName" value="provenance"/>
        <property name="metadataFields">
            <list>
                <value>dc.description.provenance</value>
            </list>
        </property>
    </bean>

    <!--Sort properties-->
    <bean id="sortTitle" class="org.dspace.discovery.configuration.DiscoverySortFieldConfiguration">
        <property name="metadataField" value="dc.title"/>
    </bean>

    <bean id="sortDateIssued" class="org.dspace.discovery.configuration.DiscoverySortFieldConfiguration">
        <property name="metadataField" value="dc.date.issued"/>
        <property name="type" value="date"/>
    </bean>
    
</beans>
Step 4 - Update localised messages.xml file
Because we introduced new discovery indexes above, we need to update the language file to present human readable messages for these new indexes.

Edit the following file:

nano $HOME/source/dspace-xmlui/src/main/webapp/i18n/messages.xml
Add the following to the bottom of the file before the closing </catalogue> tag.

<!-- Added by H Gibson -->

       <!-- Title Messages -->
        <message key="xmlui.ArtifactBrowser.ConfigurableBrowse.title.column_heading">Title</message>
        <message key="xmlui.ArtifactBrowser.ConfigurableBrowse.title.metadata.title">Browsing by Title</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.trail.metadata.title">Browsing by Title</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.sort_by.title">title</message>
	<message key="xmlui.ArtifactBrowser.AbstractSearch.sort_by.title">title</message>

       <!-- Author Messages -->
        <message key="xmlui.ArtifactBrowser.ConfigurableBrowse.author.column_heading">Author</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.title.metadata.author">Author</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.trail.metadata.author">Browsing by Author</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.sort_by.author">author</message>
	<message key="xmlui.ArtifactBrowser.AbstractSearch.sort_by.author">author</message>

       <!-- Advisor Messages -->
        <message key="xmlui.ArtifactBrowser.ConfigurableBrowse.advisor.column_heading">Advisor</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.title.metadata.advisor">Advisor</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.trail.metadata.advisor">Browsing by Advisor</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.sort_by.advisor">advisor</message>
	<message key="xmlui.ArtifactBrowser.AbstractSearch.sort_by.advisor">advisor</message>
        <message key="xmlui.ArtifactBrowser.Navigation.browse_advisor">By Advisor</message>
        <message key="xmlui.ArtifactBrowser.SimpleSearch.filter.dc.contributor.advisor">Advisor</message>
        <message key="xmlui.ArtifactBrowser.SimpleSearch.filter.advisor">Advisor</message>

       <!-- Issue Date Messages -->
        <message key="xmlui.ArtifactBrowser.ConfigurableBrowse.dateissued.column_heading">Issue Date</message>
        <message key="xmlui.ArtifactBrowser.ConfigurableBrowse.title.metadata.dateissued">Browsing by Issue Date</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.trail.metadata.dateissued">Browsing by Issue Date</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.sort_by.issuedate">issuedate</message>
	<message key="xmlui.ArtifactBrowser.AbstractSearch.sort_by.issuedate">issuedate</message>
	<message key="xmlui.ArtifactBrowser.AdvancedSearch.type_date">Date</message>
	<message key="xmlui.ArtifactBrowser.AdvancedSearch.type_issuedate">Issue Date</message>

       <!-- Subject Messages -->
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.title.metadata.subject">Subject</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.trail.metadata.subject">Browsing by Subject</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.sort_by.subject">subject</message>
	<message key="xmlui.ArtifactBrowser.AbstractSearch.sort_by.subject">subject</message>

       <!-- Type Messages -->
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.type.column_heading">Type</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.title.metadata.type">Type</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.trail.metadata.type">Browsing by Type</message>
	<message key="xmlui.ArtifactBrowser.ConfigurableBrowse.sort_by.type">type</message>
	<message key="xmlui.ArtifactBrowser.AbstractSearch.sort_by.type">type</message>
        <message key="xmlui.ArtifactBrowser.Navigation.browse_type">By Type</message>
	<message key="xmlui.ArtifactBrowser.AdvancedSearch.type_type">Type</message>	
	<message key="xmlui.ArtifactBrowser.SimpleSearch.filter.dc.type">Type</message>
	<message key="xmlui.ArtifactBrowser.SimpleSearch.filter.type">Type</message>
	<message key="xmlui.ArtifactBrowser.SimpleSearch.filter.type_filter">Type</message>

       <!-- Provenance Messages -->
	<message key="xmlui.ArtifactBrowser.AdvancedSearch.type_provenance">Provenance</message>
	<message key="xmlui.ArtifactBrowser.SimpleSearch.filter.dc.description.provenance">Provenance</message>
	<message key="xmlui.ArtifactBrowser.SimpleSearch.filter.provenance">Provenance</message>
	<message key="xmlui.ArtifactBrowser.SimpleSearch.filter.provenance_filter">Provenance</message>
