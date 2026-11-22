# Contest: woh-exp-0003

- Date: 2026-11-22
- Assessment contested: `meets_hit` (five hinge words in the first eight qualifying quotations, all `carried`)
- Recommendation: downgrade

The hit is not robust to the selection rule as registered, to the way hinge words were counted, or to the choice of lexicon, and the result it reports is one the source-critical alternative also predicts. It should be carried, at most, as a `partial`-grade instance with `discrimination: none`.

## Verification

Checked against the sources on 2026-11-22.

- **French quotations.** TBWTT-3:56 to 3:70, 3:100 to 3:157 and 3:230 to 3:262 were re-read in the `text` field of `chapter-3.json`. The eight quotations, their commentary sentences, and the six reserve candidates agree with the finding word for word.
- **Hebrew.** 1 Kings 8:10-13 and 18:38, 2 Kings 2:11, Isaiah 13:1-5 and 13:17, Psalms 19:5-7 and 33:13-14, Job 37:18 and Zechariah 5:9 were fetched from Sefaria (`/api/texts/<ref>`, Hebrew version "Miqra according to the Masorah"). Isaiah 6:1-2 was read in `isaiah-woh/chapter-6.json`. All agree with the finding.
- **Lexicon.** BDB entries for עֲרָפֶל (BibleHub 6205), תְּקוּפָה (8622) and שַׁחַק (7834) were re-fetched and read as the finding quotes them. HALOT was not reached by the Locator or by me.
- **Discrepancies.** None in quotation or locator. Points of substance follow under the objection.

## The strongest objection

**1. Under the protocol as written, the set of eight is a different set, and it contains an unresolved case.**

The protocol says a quotation qualifies if "the commentary in the same or the following paragraph" speaks of the sky or of flight. The Locator also counted commentary in the preceding paragraph, and says so. That admits 1 Kings 18:38 (comment at TBWTT-3:115, before the quotation) and 2 Kings 2:1 (comment at 3:129, before). Neither has a hinge word, so they add nothing to the tally, but they fill two of the eight places and so stop the list at Isaiah 14:13.

Applying the rule as registered, in book order:

| Quotation | Commentary | Status under the letter |
| --- | --- | --- |
| 1 Kings 8:12-13 (3:104) | 3:107, after two further quotation paragraphs | in, if 3:104-106 is read as one quotation block |
| 1 Kings 18:38 (3:116) | 3:115, preceding | out |
| 1 Kings 19:11-12 (3:120) | 3:121 | in |
| 2 Kings 2:1 (3:130-131) | 3:129, preceding | out |
| 2 Kings 2:11 (3:132) | 3:133 | in |
| Isaiah 6:1-2 (3:144) | 3:145, « réacteurs », no listed word | in, on the Locator's reading |
| Isaiah 13:4-5 (3:146) | 3:147 | in |
| Isaiah 14:13 (3:148) | 3:149 | in |
| Zechariah 5:9 (3:237) | 3:238, « combinaisons de vol » | in |
| Psalms 19:7 (3:241) | 3:242, « venus d'une planète très éloignée de l'orbite terrestre » | in |

That is eight with 1 Kings 8 and Isaiah 6 kept. If those two doubtful ones are dropped instead, Psalms 33:13-14 and Job 37:18 complete the eight. Either way **Psalms 19:7 enters the set**, and it is the case the Locator left open.

The quotation reads « (...) son point de départ est à un bout des cieux et son orbite à l'autre bout... ». The commentary: « Les créateurs sont venus d'une planète très éloignée de l'orbite terrestre. » The Hebrew is מִקְצֵה הַשָּׁמַיִם מוֹצָאוֹ וּתְקוּפָתוֹ עַל־קְצוֹתָם. BDB gives תְּקוּפָה as "coming round, circuit ... of finished circuit of sun Psalm 19:7". Two things follow. The commentary reuses « orbite » in the modern astronomical sense, of the Earth. And the possessive « son » has lost its antecedent to the opening ellipsis: in verses 5-6 it is the sun (לַשֶּׁמֶשׁ ... וְהוּא), and the commentary supplies the creators. If « orbite » is entered `shifted`, the recount gives one `shifted` in six or seven classified, which the registered criteria score as `partial`. If it is entered `carried`, the hit survives. The outcome class turns on a classification nobody has made.

**2. "Five" depends on a split.**

« un char de feu et des chevaux de feu » is one coordinated phrase of one verse, taken up by one commentary sentence. Counted as one hinge it leaves four, below the threshold, and the criteria give `partial`. The threshold of five was presumably set to guard against a hit resting on very few places. Here the five rest on four verses.

**3. Three of the five rest on picking, among the lexicon's senses, the one that matches the French.**

The `carried` class asks only that the Hebrew word have the French sense "as an ordinary lexicon sense". That is a low bar, and the Locator notes where it was only just cleared.

- « nuage » for עֲרָפֶל (1 Kings 8:12). BDB heads the entry "cloud, heavy cloud". The same BibleHub page lists the NASB renderings of the word as "thick darkness (7), thick cloud (3), thick gloom (2), deep darkness (1), gloom (1), gloomy (1)" and Strong's as "gloom ... (gross, thick) dark (cloud, -ness)". The commentary needs a cloud in the sky (« un engin en orbite ... au-dessus des nuages »). A dwelling "in thick darkness", which is how a large part of the translation tradition reads the verse, gives it nothing to work with. The classification rests on BDB alone, and the reading of the word is divided. With HALOT unconsulted this is not settled either way.
- « char » for רֶכֶב (2 Kings 2:11). BDB files this verse under the collective sense, "chariotry of fire". The French singular is what the commentary's single « engin volant » matches.
- « confins du ciel » for קְצֵה הַשָּׁמַיִם (Isaiah 13:5). The words are carried. But BDB glosses the phrase "of limits of horizon", in parallel with "a distant land", and the passage is the oracle on Babylon (13:1), whose attackers are named at 13:17 as the Medes (אֶת־מָדָי). The commentary's « on ne pouvait être plus clair » takes an idiom for earthly distance as a statement of off-world origin. The word-level class cannot register this, and it is the entire content of the reading.

None of these is a wrong entry under the protocol. Together they show that the criteria were loose enough for a literal translation to pass nearly anywhere.

**4. The alternative predicts the same.**

The source-critical account, as its proponents would put it: the author read a literal French Bible and attached technological scenarios to its images. He needs no word the translator did not supply, so the French words he touches will be in the Hebrew. What the account predicts is that the readings follow the French page and its accidents. The finding's own adjacent observations bear this out, outside the eight:

- TBWTT-3:243-245 quotes Psalms 19:5 as « il a dressé une tente sur la mer » and reads the sea as the primeval ocean. The Masoretic text has בָּהֶם, "in them". No word for "sea" stands there. Had this quotation's commentary spoken of the sky it would have been an `absent` and, under the criteria, a `miss`.
- TBWTT-3:234-235 has metric conversions, « (9 mètres) ... (4,50 mètres) », inside the guillemets of Zechariah 5:1-2.
- TBWTT-3:149 says « L'armée des cieux est décrite ici » of Isaiah 13-14, where the phrase does not occur; it occurs in the book's quotation of 1 Kings 22:19.

An all-`carried` result inside the eight is therefore what both accounts expect, and the rival note's "different in tendency" should be read as `same` for this outcome. Whether the Psalm 19:5 wording is the French Bible's or the book's was not determined; the source of the quotations (Dhorme, per `woh-claim-0066`) is held only as metadata, and no quotation was collated against it.

**5. Independence.** Same book, same speaker, same translation as `0002` and `0004`; and the faithfulness of that translation is already the content of `woh-claim-0066`.

## What the result does and does not show

It shows:

- In the eight quotations the Locator selected, the five French words or phrases the commentary takes up have Hebrew counterparts whose BDB senses include the French sense.
- The commentary names its technical objects (engin en orbite, tuyères, fusée, réacteurs) itself. They are glosses on the French image and are a lexicon sense of nothing in either language.
- Half the selected quotations have no hinge word.

It does not show:

- A hit that survives applying the selection rule as registered. That depends on Psalms 19:7.
- That the sky-arrival readings have a "Hebrew footing" in the sense the derivation wants for subclaim C. At Isaiah 13:5, the only verse in the eight whose words speak of coming from the sky, the Hebrew idiom means from far away, and the context names a human army.
- Anything that separates the claim from the source-critical alternative.

**The family taken together** (`woh-exp-0002`, `0003`, `0004`). One test, three targets, one result with three instances. In the registered scopes 22 quotations were examined; 13 have no hinge word; 11 hinge words were classified, all `carried` (4, 5, 2), with one `shifted` in a borderline set under `0004`. All three Locators independently reported that the commentary seldom takes up a word and that its re-descriptions are lexical senses of neither the French nor the Hebrew. `0003` is the only one of the three assessed as a hit, and it is so by the margin of one split phrase and one departure from the selection rule. The family should be read as a single non-discriminating result: the translation is faithful where the commentary touches it, and the readings are not lexical. It would misstate the family to report it as "one hit and two partials".

## What the ruling turns on

1. Whether the selection rule is applied as registered ("the same or the following paragraph") or as the Locator applied it. If as registered, Psalms 19:7 must be classified before any outcome can be entered, and the instance is `open` until it is.
2. Whether « char de feu » and « chevaux de feu » are two hinge words or one. If one, the registered criteria give `partial`.
3. Whether `carried` on BDB alone is accepted for עֲרָפֶל, given that the translation tradition divides between "cloud" and "thick darkness" and that the commentary's reading needs the former.
4. Whether `discrimination: partial` is kept. If the founder accepts that the source-critical account predicts `carried` here as firmly as the claim does, a ruling of `hit` would fall in the class the scoreboard reports apart and does not count as progress.
5. Whether a `narrowed` ruling is the honest form: "at the places tested, the French words are in the Hebrew", with the note that this is a statement about the translation.
