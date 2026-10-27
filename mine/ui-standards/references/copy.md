# Copy and microcopy

Write like a colleague talking across the desk: short, plain and warm. The UI's words are part of the design, and they count toward its weight.

## Rules

1. **Buttons are verb + object:** "Approve storyboard", "Open page 2", "Export CSV", "Done". Never "Submit", "OK", "Yes", or "Continue" (except as the second step of a flow). In a confirmation, the button repeats the action ("Delete project").
2. **Say a shared status once,** at the top or in the header, never on every row.
3. **Cut asides.** "(optional, saved to History)" goes. Use the field's own label and helper line only when they carry something the user needs.
4. **Errors answer three things:** what happened, why (if known) and what to do. Example: "Your card was declined. Try another card or contact your bank." Never "Something went wrong" alone, never "Oops", never an exclamation mark. Don't show an internal code as the main message; offer it as a copyable ID.
5. **Empty states say three things:** what goes here, why it matters (only if it's not obvious), and one action. Example: "No approvals waiting. New videos show up here when they're ready." Never a bare "No results"; echo the query instead ("No matches for 'tax 2024'").
6. **Loading text is specific:** "Loading payments…", not "Please wait…". Past 15s, say it's taking longer than expected.
7. **Destructive actions** name the object and the consequence: "Delete 'Q3 report'? This removes it for everyone." Prefer an Undo toast to a dialog.
8. **Titles are nouns** ("Approvals", "Library"). Subtitles describe the data, not the interface.
9. **Placeholders show a format,** not an instruction ("name@company.com").
10. **Numbers and dates** are formatted by locale, with correct plurals ("1 video", "2 videos"). Relative time switches to an absolute date after about a week. "0 seconds ago" becomes "just now".
11. **One term per concept.** Keep a short glossary in DESIGN.md (e.g. "story", not "story/clip/video" on different screens). If Save looks or reads differently in two places, one of them is wrong.
12. **Write complete, translatable strings.** No concatenated fragments. Allow 30–40% more length for translation.
13. **User content is data, never hard-coded UI copy.** Niche words, examples and source names come from the user's settings or profile, so the product works for any user.
14. **Sentence case** everywhere: headings, buttons, labels, nav.
15. **Count the words.** Before you hand a screen over, count its visible words, cut them, and count again. A product screen that explains itself in fine print is under-designed.

## The voice test

Read the screen aloud as if to the owner sitting next to you.
- If a line sounds like a system talking ("Your request has been successfully processed"), rewrite it ("Saved").
- If it sounds like marketing ("Unlock powerful insights"), delete it.
- If the same sentence appears twice, keep one.
