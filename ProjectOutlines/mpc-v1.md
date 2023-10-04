## Setup
### A. Create Bitbucket Repo
1. create repo in bitbucket `gjmarketplace`
2. CD into Projects folder
3. clone into Projects folder
4. proceed to 'Create Svelte App'
### B. Create Svelte App
1. `npm create svelte@latest gjmarketplace
	- Scaffolding:
		- "Skeleton Project"
		- "Yes, using TypeScript syntax"
		- Options: "Add ESLint"
			- `QUESTION`: should I install "Playwright for browser testing" and "Add Vitest for unit testing"?
1. `cd gjmarketplaceconsole
2. npm install
3. npm run dev


## Project Outline
### A. Architecture
1. COMPONENTS (separate .tsx files)
	1. Nav Component
	2. Filter Component
	3. Filter List Component
	4. Table Component
	5. Hubspot Component??
2. COLOR SCHEME
	1. GEO Jobe branding
	2. Calcite components????
3. CONFIGS
	1. Filter config json for filters
	2. Columns config json for table
	3. .Env??
### B. Components
1. NAV COMPONENT
	1. OAuth
	2. login/logout
	3. "Signed in with {userName}"
	4. GEO Jobe logo
3. MULTI-FILTER COMPONENT (2 parts)
	1. Filter Component (single filter)
		1. Buttons for Editing Filter
			1. edit option
			2. accept option
			3. delete option
		2. First Option: "Filter By" (dropdown/select)
			1. Product/Ecommerce Enabled/Email/Expiring/Expiration Date/Org Name/Org ID/Organizations?/Purchased/Purchase Date/Trialed/Username
		3. Second Option: Input Parameters(varies)
			1. Date (on, after, between)
			2. Timespan(last 90 days, next 90 days, this quarter, this year, last year)
			3. Select (e.g. Products -> Backup My Org)
			4. Value (input string for search)
			5. Boolean (e.g. Ecommerce Enabled -> true)
			6. With (e.g. "With multiple products", cx has AB, AC, BC, etc.)
	2. Filter List (if filters >= 0)
		1. concats/joins multiple filters to send to to API and filters to table
	3. `FEATURES:
				1. "ENTER" key-pressed for value fields
				2. Default option is PRODUCTS
				3. Fuzzy search for value inputs
				4. "Loading" widget/icon
				5. 
4. TABLE COMPONENT
	1. Columns
		1. ID: index
		2. hubspot: icon if cx exists in our HubSpot directory
		3. customer: provision.purchaserFullName
		4. email: provision.purchaserEmail
		5. organization: customer.name
		6. orgID: provision.purchaserOrgId
		7. listingName: provision.title
		8. startDate: provision.startDate
		9. endDate: provision.endDate
		10. ecommerceEnabled: listing.ecommerceEnabled
		11. licenseType: provision.purchased/trial
		12. actions: provision.actions/delete or start provision
	2. `FEATURES:
		1. Alternating line colors
		2. Filtering begins on keypresses for value inputs
		3. Hubspot column
		4. Provision Items column 
		5. CX Tags
		6. CX Not
### C. Testing
  - TBD

## GAMEPLAN
1. Setup file structure
	1. GJMarketplace
		1. .git
		2. build
		3. node_modules
		4. public
			1. assets
		5. src
			1. table.tsx
			2. filter.tsx
			3. filterList.tsx
			4. hubspot.tsx
			5. filterConfig.json
			6. columnsConfig.json
		6. index.html
		7. tsconfig.json
		8. package.json
		9. package-lock.json
		10. .gitignore
		11. README.md
2. Create HTML
	1. (tickets)
3. Create NAV
	1. add oauth
	2. (tickets)
4. Create TABLE
	1. (tickets)
5. Create FILTER
	1. (tickets)
6. Create FILTER LIST
	1. (tickets)
7. Create HUBSPOT
()	1. (tickets)

### Tickets:
# ()
Sprint 1:
1. create project
2. implement a simple OAUTH 
	2. Use a store for this.  That way any file that needs auth can access it.
3. create simple table component and table store that loads and displays the data.  
	1. I'll show you how to make a good table store
	2. Table store handles all the data and the Table component is just displaying that data
	3. You'll want to make interfaces for everything
	4. Probably want to paginate the data, so you only query like 20 records at a time.
	5. Basic CSS, nothing fancy yet.
	6. HTML Table element is perfect for this

Sprint 2:
1. Create Filter List & Filter component:
	1. Start simple, add like two or three filters
	3. Each filter should interact with the table store directly.  That way the table store can update the list
	2. the filter list will essentially just be a div.  No component parameters needed if you use the table store
	4. Instead of trying to make one filter component that works for every filter.  It might be easier to just make each type of filter it's own component.  At least at first.
	5. All the filter logic will be inside the table store, so all the filters need to do is relay the input to that.

Sprint 3:
1. Start cleaning up the look of the app:
	1. add login button / Nav bar
	2. CSS and little things
 2. Start thinking about adding the config files back
