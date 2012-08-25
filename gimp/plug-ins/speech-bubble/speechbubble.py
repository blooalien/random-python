#!/usr/bin/env python

#	Title: Simple Speech Bubble
#	Author: Bavarin Fleetfoot <bavarin.fleetfoot@hotmail.com>
#	License: http://creativecommons.org/publicdomain/zero/1.0/

from gimpfu import *

def speechbubble(image, drawable, radius):
	gimp.context_push()
	image.undo_group_start()

	pdb.gimp_edit_fill(drawable, FOREGROUND_FILL)
	pdb.gimp_selection_shrink(image, radius)
	pdb.gimp_edit_fill(drawable, BACKGROUND_FILL)

	image.undo_group_end()
	gimp.context_pop()

register(
	"speech-bubble",
	"Cartoon Speech Bubble",
	"Add a cartoon speech bubble using the current selection.",
	"Bavarin Fleetfoot",
	"Public Domain",
	"2011",
	"<Image>/Filters/Render/Speech Bubble...",
	"*",
	[
		(PF_SPINNER, 'radius', 'Line Stroke Size', 2, (1,6,1))
	],
	[],
	speechbubble,
	)

main()
