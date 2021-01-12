
search_res = ''' 
	<div id="item_res" class="x-container x-padding x-col l6 x-animate-opacity">
		<div class="x-round-large x-card x-hover-greyscale x-card x-hover-shadow x-container x-topbar x-border-{} x-card" style='height:250px'
			onclick = "open_modal_pdf_view('{}','{}')">
			<div class="x-container x-padding x-col l6">
				<span class="x-text-blue x-small"><b>{}</b></span><br>
				<span class="x-small x-text-grey">{}</span><hr>
				<span class="x-text-grey x-small">Date Uploaded : <b class="x-text-black">{}</b></span><br>
			</div>
			<div class="x-container x-padding x-small x-col l6">
				<span class="x-small x-text-grey">Municipality : <b>{}</b></span><br>
				<span class="x-small x-text-grey">Brgy : <b>{}</b></span><br>
				<span class="x-small x-text-grey">Modality : <b>{}</b></span><br>
				<span class="x-small x-text-grey">Cycle : <b>{}</b></span><br>
				<span class="x-small x-text-grey">CADT#: <b>{}</b></span><br>
			</div>
		</div>
	</div>
'''

search_res_new = '''
	<div id="item_res" class="x-container x-padding x-row x-animate-opacity">
		<div class="x-card x-hover-greyscale x-card x-hover-shadow x-container x-topbar x-border-{} x-card" 
			onclick = "open_modal_pdf_view('{}','{}')">
			<div class="x-container x-padding x-col l4">
				<span class="x-text-blue x-small"><b>{}</b></span><br>
				<span class="x-small x-text-grey">{}</span><hr>
				<span class="x-text-grey x-small">Date Uploaded : <b class="x-text-black">{}</b></span><br>
			</div>
			<div class="x-container x-padding x-small x-col l4">
				<span class="x-small x-text-grey">Municipality : <b>{}</b></span><br>
				<span class="x-small x-text-grey">Brgy : <b>{}</b></span><br>
				<span class="x-small x-text-grey">Modality : <b>{}</b></span><br>
			</div>
			<div class="x-container x-padding x-small x-col l4">
				<span class="x-small x-text-grey">Cycle : <b>{}</b></span><br>
				<span class="x-small x-text-grey">CADT#: <b>{}</b></span><br>
			</div>
		</div>
	</div>
'''


finding_res = '''
	<div class="x-container x-padding">
		<div class="x-container x-row x-white x-card x-hover-shadow" onclick="view_findings('{}')">
			<div class="x-third x-padding x-leftbar x-border-green">
				<b>{}</b><br>
				<span class="x-text-grey">
					<span>{}</span>  |
					<span>{}</span> | 
					<span>{}</span><br>
					<span class="x-text-grey">
						Findings :
						<span class="x-text-black">{}</span>
					</span>
				</span>
			</div>
			<div class="x-third x-padding x-leftbar x-border-red">
				<span>{}</span><br> 
				<span class="x-text-grey">
					<span>Tranch : <span class='x-text-black'>{}</span></span>  |
					<span>Date Encoded : <span class='x-text-black'>{}</span></span>
				</span>
			</div>
			<div class="x-third x-padding x-leftbar x-border-orange">
				<span class="x-text-grey">
					<span>DV #: : <span class='x-text-black'>{}</span></span> <br>
					<span>SP # : <span class='x-text-black'>{}</span></span><br> 
					<span>RFR #: <span class='x-text-black'>{}</span></span>
				</span>
			</div>
		</div>
	</div>
'''