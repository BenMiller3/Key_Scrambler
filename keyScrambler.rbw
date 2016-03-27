Shoes.app(title: "Keyboard Scrambler",width: 500, height: 300,resizable: false){
	
	background("background.png")
	
	stack(margin: 170, margin_bottom: 0, margin_top: 110){
	
	@btt1 = button "Scramble Keyboard"
	para strong ""
	@btt2 = button " Revert to Normal"
	
	}
	
	@btt1.click{
	
	#runs the scrambler script and remaps keys
	`BeginScramble.exe`
	
	}
	
	@btt2.click{
	
	# ends the scrambler script and ends hotkey remapper
	`EndScramble.exe`

	}
	
}


